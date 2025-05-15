"""
    Поиск ключевых звеньев
"""

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

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# Инициализация новому свойству friends каждого пользователя пустой список:
friendships = {user["id"]: [] for user in users}

# Заполнение списков данными из списка кортежей friendships:
for i, j in friendship_pairs:
    friendships[i].append(j)  # Добавить j как друга для i
    friendships[j].append(i)  # Добавить i как друга для j


# Число друзей
def number_of_friends(user):
    # Сколько друзей есть у пользователя user?
    user_id = user["id"]
    friend_ids = friendships[user_id]

    # Длина списка id друзей
    return len(friend_ids)


# общее число связей = 24
total_connections = sum(number_of_friends(user)
                        for user in users)

# Длина списка друзей
num_users = len(users)
# Cреднее число связей (24 / 10 == 2.4)
avg_connections = total_connections / num_users

# Cоздать список в формате (id пользователя, число друзей)
num_friends_by_id = [(user["id"], number_of_friends(user))
                     for user in users]

num_friends_by_id.sort(  # упорядочить его
    key=lambda id_and_friends: id_and_friends[1],  # по полю num_friends
    reverse=True)  # в убывающем порядке

"""
    Аналитики, которых Вы должны знать
"""


# Список id друзей пользователя user (плохой вариант)
def friend_of_a_friend_ids_bad(user):
    return [foaf_id
            for friend_id in friendships[user["id"]]
            for foaf_id in friendships[friend_id]]


# Функция friend_of_a_friend_ids_bad(users[0]) == [0, 2, 3, 0, 1, 3]

print(friendships[0])  # [1, 2]
print(friendships[1])  # [0, 2, 3]
print(friendships[2])  # [0, 1, 3]

# Словарь Counter не загружается по умолчанию не тот же самый
from collections import Counter


def friends_of_friends(user):
    user_id = user["id"]

    return Counter(
        foaf_id
        for friend_id in friendships[user_id]  # Для каждого моего друга
        for foaf_id in friendships[friend_id]  # подсчитать ИХ друзей,
        if foaf_id != user_id  # которые не являются мной
        and foaf_id not in friendships[user_id]  # и не мои друзья
    )


print(friends_of_friends(users[3]))  # Counter({0: 2, 5: 1})

# Интересующие темы
interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]


# Аналитики, которым нравится целевая тема target_interest
def data_scientists_who_like(target_interest):
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]


from collections import defaultdict

# id пользователей по значению темы
# Ключи - это интересующие темы, значения - это списки из id пользователей, интересующихся этой темой
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

# Идентификаторы тем по идентификатору пользователя
# Ключи - это id пользователей, значения – списки тем для конкретного id
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)


# Наиболее общие интересующие темы с пользователем user
def most_common_interests_with(user):
    return Counter(
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
    )


"""
    Зарплаты и опыт работы
"""
# Зарплаты и стаж
salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

# Зарплата в зависимости от стажа
# Ключи - это годы, значения - это списки зарплат для каждого стажа
salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

# Средняя зарплата в зависимости от стажа
# Ключи - это годы, каждое значение - это средняя зарплата по этому стажу
average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}


# 0.7: 48000.0,
# 1.9: 48000.0,
# 2.5: 60000.0,
# 4.2: 63000.0,
# 6: 76000.0,
# 6.5: 69000.0,
# 7.5: 76000.0,
# 8.1: 88000.0,
# 8.7: 83000.0,
# 10: 83000.0

# Стажная группа
def tenure_bucket(tenure):
    if tenure < 2:
        return "Менее двух"
    elif tenure < 5:
        return "Между двумя и пятью"
    else:
        return "Более пяти"


# Зарплата в зависимости от стажной группы
# Ключи = стажные группы, значения = списки зарплат в этой группе
# Словарь содержит списки зарплат, соответствующие каждой стажной группе
salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

# Средняя зарплата по группе
# Ключи = стажные группы, значения = средняя зарплата по этой группе
average_salary_by_bucket = {
    tenure_bucket: sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}

# Менее двух: 48000.0,
# Между двумя и пятью: 61500.0,
# Более пяти: 79166.66666666667


"""
    Оплата премиум-аккаунтов
"""


# 0.7: 48000.0,
# 1.9: 48000.0,
# 2.5: 60000.0,
# 4.2: 63000.0,
# 6: 76000.0,
# 6.5: 69000.0,
# 7.5: 76000.0,
# 8.1: 88000.0,
# 8.7: 83000.0,
# 10: 83000.0

def predict_paid_or_unpaid(years_experience):
    if years_experience < 3.0:
        return "paid"
    elif years_experience < 8.5:
        return "unpaid"
    else:
        return "paid"


"""
    Популярные темы
"""

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

# Cлова и частотности
words_and_counts = Counter(word
                           for user, interest in interests
                           for word in interest.lower().split())

for word, count in words_and_counts.most_common():
    if count > 1:
        print(word, count)

# learning 3
# java 3
# python 3
# big 3
# data 3
# hbase 2
# regression 2
# cassandra 2
# statistics 2
# probability 2
# hadoop 2
# networks 2
# machine 2
# neural 2
# scikit-learn 2
# r 2
