# !!! Необходимо создать папку im в корне проекта для сохранения графиков !!!

from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

plt.title("Номинальный ВВП")

plt.ylabel("Млрд $")
# plt.show()

plt.savefig('im/1_Номинальный_ВВП.png')
plt.gca().clear()

"""
    Столбчатые диаграммы
"""

movies = ["Энни Холл", "Бен-Гур", "Касабланка", "Ганди", "Вестсайдская история"]
num_oscars = [5, 11, 3, 8, 10]

plt.bar(range(len(movies)), num_oscars)

plt.title("Мои любимые фильмы")
plt.ylabel("Количество наград")

plt.xticks(range(len(movies)), movies)
# plt.show()

plt.savefig('im/2_Фильмы.png')
plt.gca().clear()

from collections import Counter

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)

plt.bar([x + 5 for x in histogram.keys()],
        histogram.values(),
        10,
        edgecolor=(0, 0, 0))

plt.axis([-5, 105, 0, 5])

plt.xticks([10 * i for i in range(11)])
plt.xlabel("Дециль")
plt.ylabel("Число студентов")
plt.title("Распределение оценок за экзамен №1")
# plt.show()

plt.savefig('im/3_Оценки.png')
plt.gca().clear()

mentions = [500, 505]
years = [2017, 2018]

plt.bar(years, mentions, 0.8)
plt.xticks(years)
plt.ylabel("Число упоминаний науки о данных")

plt.ticklabel_format(useOffset=False)

plt.axis([2016.5, 2018.5, 499, 506])
plt.title("Какой 'огромный' прирост!")
# plt.show()

plt.savefig('im/4_Вводящая_в_заблуждение_ось_y.png')
plt.gca().clear()

plt.bar(years, mentions, 0.8)
plt.xticks(years)
plt.ylabel("Число упоминаний науки о данных")
plt.ticklabel_format(useOffset=False)

plt.axis([2016.5, 2018.5, 0, 550])
plt.title("Больше не такой огромный")
# plt.show()

plt.savefig('im/5_Не_вводящая_в_заблуждение_ось_y.png')
plt.gca().clear()

"""
    Линейные графики
"""

variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

plt.plot(xs, variance, 'g-', label='дисперсия')
plt.plot(xs, bias_squared, 'r-.', label='смещение^2')
plt.plot(xs, total_error, 'b:', label='суммарная ошибка')

plt.legend(loc=9)
plt.xlabel("Сложность модели")
plt.xticks([])
plt.title("Компромисс между смещением и дисперсией")
# plt.show()

plt.savefig('im/6_Линейная_диаграмма.png')
plt.gca().clear()

"""
    Точечные диаграммы
"""

friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
                 xy=(friend_count, minute_count),
                 xytext=(5, -5),
                 textcoords='offset points')

plt.title("Зависимость между количеством минут и числом друзей")
plt.xlabel("Число друзей")
plt.ylabel("Время, проводимое на сайте ежедневно, мин")
# plt.show()

plt.savefig('im/7_Диаграмма_рассеяния.png')
plt.gca().clear()

test_1_grades = [99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]

plt.scatter(test_1_grades, test_2_grades)
plt.title("Несопоставимые оси")
plt.xlabel("Оценки за тест №1")
plt.ylabel("Оценки за тест №2")
# plt.show()

plt.savefig('im/8_Несопоставимые_оси_диаграммы_рассеяния.png')
plt.gca().clear()

test_1_grades = [99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]
plt.scatter(test_1_grades, test_2_grades)
plt.title("Сопоставимые оси")
plt.axis("equal")
plt.xlabel("Оценки за тест №1")
plt.ylabel("Оценки за тест №2")
# plt.show()

plt.savefig('im/9_Сопоставимые_оси_диаграммы_рассеяния.png')
plt.gca().clear()
