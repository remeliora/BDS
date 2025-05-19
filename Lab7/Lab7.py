import math
import random
from collections import Counter
from typing import List, Tuple, Callable

import matplotlib.pyplot as plt


# Вспомогательные функции
def shape(matrix: List[List[float]]) -> Tuple[int, int]:
    """Возвращает (число строк, число столбцов) матрицы"""
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if matrix else 0
    return num_rows, num_cols


def get_column(matrix: List[List[float]], j: int) -> List[float]:
    """Возвращает j-й столбец матрицы"""
    return [row[j] for row in matrix]


def make_matrix(num_rows: int, num_cols: int, entry_fn: Callable[[int, int], float]) -> List[List[float]]:
    """Создает матрицу num_rows x num_cols, где элемент (i,j) - entry_fn(i,j)"""
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]


def inverse_normal_cdf(p: float, mu: float = 0, sigma: float = 1, tolerance: float = 0.00001) -> float:
    """Аппроксимация обратной функции нормального распределения"""
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z, low_p = -10.0, 0
    hi_z, hi_p = 10.0, 1

    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            hi_z, hi_p = mid_z, mid_p
        else:
            break
    return mid_z


def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    """Кумулятивная функция распределения для нормального распределения"""
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


def mean(xs: List[float]) -> float:
    """Среднее значение"""
    return sum(xs) / len(xs)


def de_mean(xs: List[float]) -> List[float]:
    """Транслировать xs путем вычитания его среднего (результат имеет среднее 0)"""
    x_bar = mean(xs)
    return [x - x_bar for x in xs]


def dot(v: List[float], w: List[float]) -> float:
    """Скалярное произведение"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def covariance(xs: List[float], ys: List[float]) -> float:
    """Ковариация"""
    return dot(de_mean(xs), de_mean(ys)) / (len(xs) - 1)


def standard_deviation(xs: List[float]) -> float:
    """Стандартное отклонение"""
    return math.sqrt(covariance(xs, xs))


def correlation(xs: List[float], ys: List[float]) -> float:
    """Корреляция Пирсона"""
    stdev_x = standard_deviation(xs)
    stdev_y = standard_deviation(ys)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(xs, ys) / stdev_x / stdev_y
    else:
        return 0


def random_normal() -> float:
    """Возвращает случайную выборку из стандартного нормального распределения"""
    return inverse_normal_cdf(random.random())


# Функции для одномерных данных
def bucketize(point: float, bucket_size: float) -> float:
    """Округлить точку до следующего наименьшего кратного размера интервала bucket_size"""
    return bucket_size * math.floor(point / bucket_size)


def make_histogram(points: List[float], bucket_size: float) -> Counter:
    """Сгруппировать точки и подсчитать количество в интервале"""
    return Counter(bucketize(point, bucket_size) for point in points)


def plot_histogram(points: List[float], bucket_size: float, title: str = "", filename: str = None) -> None:
    """Изобразить гистограмму и сохранить в файл"""
    histogram = make_histogram(points, bucket_size)
    plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
    plt.title(title)
    if filename:
        plt.savefig(filename)
        plt.close()
    else:
        plt.show()


# Функции для двумерных данных
def scatter_plot(xs: List[float], ys1: List[float], ys2: List[float], title: str = "", filename: str = None) -> None:
    """Точечная диаграмма для двух наборов данных"""
    plt.scatter(xs, ys1, marker='.', color='black', label='ys1')
    plt.scatter(xs, ys2, marker='.', color='gray', label='ys2')
    plt.xlabel('xs')
    plt.ylabel('ys')
    plt.legend(loc=9)
    plt.title(title)
    if filename:
        plt.savefig(filename)
        plt.close()
    else:
        plt.show()


# Функции для многомерных данных
def correlation_matrix(data: List[List[float]]) -> List[List[float]]:
    """Возвращает матрицу num_columns x num_columns, где запись
    в ячейке (i, j) - это корреляция между столбцами i и j данных"""
    _, num_columns = shape(data)

    def matrix_entry(i: int, j: int) -> float:
        return correlation(get_column(data, i), get_column(data, j))

    return make_matrix(num_columns, num_columns, matrix_entry)


def plot_scatter_matrix(data: List[List[float]], filename: str = None) -> None:
    """Точечная матрица для многомерных данных"""
    _, num_columns = shape(data)
    fig, ax = plt.subplots(num_columns, num_columns, figsize=(10, 10))

    for i in range(num_columns):
        for j in range(num_columns):
            if i != j:
                ax[i][j].scatter(get_column(data, j), get_column(data, i))
            else:
                ax[i][j].annotate("серия " + str(i), (0.5, 0.5),
                                  xycoords='axes fraction',
                                  ha="center", va="center")

            if i < num_columns - 1: ax[i][j].xaxis.set_visible(False)
            if j > 0: ax[i][j].yaxis.set_visible(False)

    ax[-1][-1].set_xlim(ax[0][-1].get_xlim())
    ax[0][0].set_ylim(ax[0][1].get_ylim())

    if filename:
        plt.savefig(filename)
        plt.close()
    else:
        plt.show()


# Примеры использования
if __name__ == "__main__":
    random.seed(0)

    # Одномерные данные
    uniform = [200 * random.random() - 100 for _ in range(10000)]
    normal = [57 * inverse_normal_cdf(random.random()) for _ in range(10000)]

    print("Среднее uniform:", mean(uniform))
    print("Стандартное отклонение uniform:", standard_deviation(uniform))
    print("Среднее normal:", mean(normal))
    print("Стандартное отклонение normal:", standard_deviation(normal))

    plot_histogram(uniform, 10, "Гистограмма равномерных случайных величин",
                   "1_Гистограмма_равномерных_случайных_величин.png")
    plot_histogram(normal, 10, "Гистограмма нормальных случайных величин",
                   "2_Гистограмма_нормальных_случайных_величин.png")

    # Двумерные данные
    xs = [inverse_normal_cdf(random.random()) for _ in range(1000)]
    ys1 = [x + random_normal() / 2 for x in xs]
    ys2 = [-x + random_normal() / 2 for x in xs]

    print("Корреляция xs и ys1:", correlation(xs, ys1))
    print("Корреляция xs и ys2:", correlation(xs, ys2))

    scatter_plot(xs, ys1, ys2, "Очень разное совместное распределение", "3_Очень_разное_совместное_распределение.png")

    # Многомерные данные
    data = [
        xs,
        ys1,
        ys2,
        [random.choice([0, 6]) for _ in range(1000)]
    ]
    data = list(zip(*data))  # Транспонирование матрицы

    print("Точечная матрица:")
    print(correlation_matrix(data))

    plot_scatter_matrix(data, "4_Точечная матрица.png")
