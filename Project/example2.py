import math, random, re
from collections import defaultdict, Counter, deque
from linear_algebra import dot, get_row, get_column, make_matrix, magnitude, scalar_multiply, shape, distance
from functools import partial
import networkx as nx
import matplotlib.pyplot as plt

users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# give each user a friends list
for user in users:
    user["friends"] = []

# and populate it
for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])


#
# Betweenness Centrality
#
def shortest_paths_from(from_user):
    shortest_paths_to = {from_user["id"]: [[]]}
    frontier = deque((from_user, friend) for friend in from_user["friends"])

    while frontier:
        prev_user, user = frontier.popleft()
        user_id = user["id"]
        paths_to_prev = shortest_paths_to[prev_user["id"]]
        paths_via_prev = [path + [user_id] for path in paths_to_prev]

        old_paths_to_here = shortest_paths_to.get(user_id, [])
        min_path_length = len(old_paths_to_here[0]) if old_paths_to_here else float('inf')

        new_paths_to_here = [path for path in paths_via_prev
                             if len(path) <= min_path_length and path not in old_paths_to_here]
        shortest_paths_to[user_id] = old_paths_to_here + new_paths_to_here

        frontier.extend((user, friend) for friend in user["friends"]
                        if friend["id"] not in shortest_paths_to)
    return shortest_paths_to


for user in users:
    user["shortest_paths"] = shortest_paths_from(user)

for user in users:
    user["betweenness_centrality"] = 0.0

for source in users:
    source_id = source["id"]
    for target_id, paths in source["shortest_paths"].items():
        if source_id < target_id:
            num_paths = len(paths)
            contrib = 1 / num_paths
            for path in paths:
                for id in path:
                    if id not in [source_id, target_id]:
                        users[id]["betweenness_centrality"] += contrib


#
# closeness centrality
#
def farness(user):
    return sum(len(paths[0]) for paths in user["shortest_paths"].values())


for user in users:
    user["closeness_centrality"] = 1 / farness(user)


#
# matrix multiplication
#
def matrix_product_entry(A, B, i, j):
    return dot(get_row(A, i), get_column(B, j))


def matrix_multiply(A, B):
    n1, k1 = shape(A)
    n2, k2 = shape(B)
    if k1 != n2:
        raise ArithmeticError("incompatible shapes!")
    return make_matrix(n1, k2, partial(matrix_product_entry, A, B))


def vector_as_matrix(v):
    return [[v_i] for v_i in v]


def vector_from_matrix(v_as_matrix):
    return [row[0] for row in v_as_matrix]


def matrix_operate(A, v):
    v_as_matrix = vector_as_matrix(v)
    product = matrix_multiply(A, v_as_matrix)
    return vector_from_matrix(product)


def find_eigenvector(A, tolerance=0.00001):
    guess = [1 for __ in A]
    while True:
        result = matrix_operate(A, guess)
        length = magnitude(result)
        next_guess = scalar_multiply(1 / length, result)
        if distance(guess, next_guess) < tolerance:
            return next_guess, length
        guess = next_guess


#
# eigenvector centrality
#
def entry_fn(i, j):
    return 1 if (i, j) in friendships or (j, i) in friendships else 0


n = len(users)
adjacency_matrix = make_matrix(n, n, entry_fn)
eigenvector_centralities, _ = find_eigenvector(adjacency_matrix)

#
# directed graphs
#
endorsements = [(0, 1), (1, 0), (0, 2), (2, 0), (1, 2), (2, 1), (1, 3),
                (2, 3), (3, 4), (5, 4), (5, 6), (7, 5), (6, 8), (8, 7), (8, 9)]

for user in users:
    user["endorses"] = []
    user["endorsed_by"] = []

for source_id, target_id in endorsements:
    users[source_id]["endorses"].append(users[target_id])
    users[target_id]["endorsed_by"].append(users[source_id])

endorsements_by_id = [(user["id"], len(user["endorsed_by"])) for user in users]
sorted(endorsements_by_id, key=lambda pair: pair[1], reverse=True)


def page_rank(users, damping=0.85, num_iters=100):
    num_users = len(users)
    pr = {user["id"]: 1 / num_users for user in users}
    base_pr = (1 - damping) / num_users

    for __ in range(num_iters):
        next_pr = {user["id"]: base_pr for user in users}
        for user in users:
            links_pr = pr[user["id"]] * damping
            for endorsee in user["endorses"]:
                next_pr[endorsee["id"]] += links_pr / len(user["endorses"])
        pr = next_pr
    return pr


# ====================== ВИЗУАЛИЗАЦИЯ ГРАФОВ ======================
def normalize_sizes(sizes, min_size=300, max_size=3000):
    min_val, max_val = min(sizes.values()), max(sizes.values())
    if min_val == max_val:
        return {k: (min_size + max_size) / 2 for k in sizes}
    return {node: min_size + (max_size - min_size) *
                  (size - min_val) / (max_val - min_val)
            for node, size in sizes.items()}


def visualize_undirected_graph(metric, title, filename, pos):
    G = nx.Graph()
    G.add_nodes_from(range(len(users)))
    G.add_edges_from(friendships)

    sizes_dict = normalize_sizes(metric)
    sizes = [sizes_dict[node] for node in G.nodes()]

    plt.figure(figsize=(10, 8))
    nx.draw_networkx(
        G, pos,
        node_size=sizes,
        with_labels=True,
        font_weight='bold',
        node_color='skyblue'
    )
    plt.title(title)
    plt.axis('off')
    plt.savefig(filename, format='PNG')
    plt.close()


def visualize_directed_graph(metric, title, filename, pos):
    DG = nx.DiGraph()
    DG.add_nodes_from(range(len(users)))
    DG.add_edges_from(endorsements)

    sizes_dict = normalize_sizes(metric)
    sizes = [sizes_dict[node] for node in DG.nodes()]

    plt.figure(figsize=(10, 8))
    nx.draw_networkx(
        DG, pos,
        node_size=sizes,
        arrows=True,
        arrowstyle='->',
        arrowsize=20,
        with_labels=True,
        font_weight='bold',
        node_color='lightgreen'
    )
    plt.title(title)
    plt.axis('off')
    plt.savefig(filename, format='PNG')
    plt.close()


def visualize_authority_graph(pos):
    DG = nx.DiGraph()
    DG.add_nodes_from(range(len(users)))
    DG.add_edges_from(endorsements)

    # Рассчитываем авторитетность через HITS
    authorities = nx.hits(DG)[1]
    sizes_dict = normalize_sizes(authorities)
    sizes = [sizes_dict[node] for node in DG.nodes()]

    plt.figure(figsize=(10, 8))
    nx.draw_networkx(
        DG, pos,
        node_size=sizes,
        arrows=True,
        arrowstyle='->',
        arrowsize=20,
        with_labels=True,
        font_weight='bold',
        node_color='salmon'
    )
    plt.title("Authority Scores (HITS)")
    plt.axis('off')
    plt.savefig("authority_scores.png", format='PNG')
    plt.close()


# ====================== ОСНОВНАЯ ПРОГРАММА ======================
if __name__ == "__main__":
    # Создаем базовый граф для определения позиций
    G_base = nx.Graph()
    G_base.add_nodes_from(range(len(users)))
    G_base.add_edges_from(friendships)
    pos = nx.spring_layout(G_base, seed=42)  # Фиксируем позиции

    # Визуализация базового графа
    plt.figure(figsize=(10, 8))
    nx.draw_networkx(
        G_base, pos,
        node_size=1000,
        with_labels=True,
        font_weight='bold',
        node_color='lightgray'
    )
    plt.title("DataSciencester Network")
    plt.axis('off')
    plt.savefig("base_network.png", format='PNG')
    plt.close()

    # Вывод метрик и визуализация
    print("Betweenness Centrality")
    betweenness_metric = {}
    for user in users:
        print(user["id"], user["betweenness_centrality"])
        betweenness_metric[user["id"]] = user["betweenness_centrality"]
    visualize_undirected_graph(
        betweenness_metric,
        "Betweenness Centrality",
        "betweenness_centrality.png",
        pos
    )
    print()

    print("Closeness Centrality")
    closeness_metric = {}
    for user in users:
        print(user["id"], user["closeness_centrality"])
        closeness_metric[user["id"]] = user["closeness_centrality"]
    visualize_undirected_graph(
        closeness_metric,
        "Closeness Centrality",
        "closeness_centrality.png",
        pos
    )
    print()

    print("Eigenvector Centrality")
    eigenvector_metric = {i: eigenvector_centralities[i] for i in range(len(users))}
    for user_id, centrality in enumerate(eigenvector_centralities):
        print(user_id, centrality)
    visualize_undirected_graph(
        eigenvector_metric,
        "Eigenvector Centrality",
        "eigenvector_centrality.png",
        pos
    )
    print()

    print("PageRank")
    pagerank_metric = page_rank(users)
    for user_id, pr in pagerank_metric.items():
        print(user_id, pr)
    visualize_directed_graph(
        pagerank_metric,
        "PageRank",
        "pagerank.png",
        pos
    )
    print()

    # Визуализация авторитетности
    visualize_authority_graph(pos)
