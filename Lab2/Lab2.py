"""
    Пробельные символы
"""
# Пример отступов во вложенных циклах for
for i in [1, 2, 3, 4, 5]:
    print(i)  # первая строка в блоке for i
    for j in [1, 2, 3, 4, 5]:
        print(j)  # первая строка в блоке for j
        print(i + j)  # последняя строка в блоке for j
    print(i)  # последняя строка в блоке for i
print("Циклы закончились")

# Пример многословного выражения
long_winded_computation = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 +
                           13 + 14 + 15 + 16 + 17 + 18 + 19 + 20)

# Список списков
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Такой список списков легче читается
easier_to_read_list_of_lists = [[1, 2, 3],
                                [4, 5, 6],
                                [7, 8, 9]]

for i in [1, 2, 3, 4, 5]:
    # обратите внимание на пустую строку
    print(i)

"""
    Модули
"""

import re

my_regex = re.compile("[0-9]+", re.I)

import re as regex

my_regex = regex.compile("[0-9]+", regex.I)

from collections import defaultdict, Counter

lookup = defaultdict(int)
my_counter = Counter()

match = 10
from re import *  # в модуле re есть функция match

print(match)  # <function match at 0x00000180A71849D0>

"""
    Функции
"""


def double(x):
    """
    Здесь, когда нужно, размещают
    многострочный документирующий комментарий docstring,
    который поясняет, что именно функция вычисляет.
    Например, данная функция умножает входящее значение на 2
    """
    return x * 2


# применить функцию f к единице
def apply_to_one(f):
    """
    Вызывает функцию f с единицей в качестве аргумента
    """
    return f(1)


my_double = double  # Ссылка на ранее определенную функцию
x = apply_to_one(my_double)  # = 2

y = apply_to_one(lambda x: x + 4)  # = 5

# Так не делать
another_double = lambda x: 2 * x


# Лучше так
def another_double(x):
    return 2 * x


def my_print(message="Мое сообщение по умолчанию"):
    print(message)


my_print("hello")  # Напечатает "hello"
my_print()  # Напечатает "Мое сообщение по умолчанию"


# Функция вычитания
def subtract(a=0, b=0):
    return a - b


subtract(10, 5)  # возвращает 5
subtract(0, 5)  # возвращает -5
subtract(b=5)  # то же, что и в предыдущем примере

"""
    Строки
"""

single_quoted_string = 'Наука о данных'  # Одинарные
double_quoted_string = "Наука о данных"  # Двойные

tab_string = "\t"  # Обозначает символ табуляции
len(tab_string)  # = 1

not_tab_string = r"\t"  # Обозначает символы '\' and 't'
len(not_tab_string)  # = 2

multi_line_string = """Это первая строка.
это вторая строка,
а это третья строка"""

"""
    Исключения
"""

try:
    print(0 / 0)
except ZeroDivisionError:
    print("Нельзя делить на ноль")

"""
    Списки
"""

integer_list = [1, 2, 3]  # Список целых чисел
heterogeneous_list = ["string", 0.1, True]  # Разнородный список
list_of_lists = [integer_list, heterogeneous_list, []]  # Список списков

list_length = len(integer_list)  # Длина списка = 3
list_sum = sum(integer_list)  # Сумма значений в списке = 6

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

zero = x[0]  # = 0, списки нуль-индексные, т. е. индекс 1-го элемента = 0
one = x[1]  # = 1
nine = x[-1]  # = 9, по-питоновски взять последний элемент
eight = x[-2]  # = 8, по-питоновски взять предпоследний элемент
x[0] = -1  # теперь x=[-1, 1, 2, 3, ..., 9]

first_three = x[:3]  # [-1, 1, 2]
three_to_end = x[3:]  # [3, 4, ..., 9]
one_to_four = x[1:5]  # [1, 2, 3, 4]
last_three = x[-3:]  # [7, 8, 9]
without_first_and_last = x[1:-1]  # [1, 2, ..., 8]
copy_of_x = x[:]  # [-1, 1, 2, ..., 9]

every_third = x[::3]  # [-1, 3, 6, 9]
five_to_three = x[5:2:-1]  # [5, 4, 3]

1 in [1, 2, 3]  # True
0 in [1, 2, 3]  # False

x = [1, 2, 3]
x.extend([4, 5, 6])  # теперь x =  [1, 2, 3, 4, 5, 6]

x = [1, 2, 3]
x.append(0)  # теперь x [1, 2, 3, 0]
y = x[-1]  # = 0
z = len(x)  # = 4

x, y = [1, 2]  # теперь x = 1, y = 2

_, y = [1, 2]  # теперь y == 2, первый элемент не нужен

"""
    Кортежи
"""
my_list = [1, 2]  # задать список
my_tuple = (1, 2)  # задать кортеж
other_tuple = 3, 4  # еще один кортеж
my_list[1] = 3  # теперь my_list = [1, 3]

try:
    my_tuple[1] = 3
except TypeError:
    print("Кортеж изменять нельзя")


# Функция возвращает сумму и произведение двух параметров
def sum_and_product(x, y):
    return (x + y), (x * y)


sp = sum_and_product(2, 3)  # = (5, 6)
s, p = sum_and_product(5, 10)  # s = 15, p = 50

x, y = 1, 2  # теперь x = 1, y = 2
x, y = y, x  # Обмен переменными по-питоновски; теперь x = 2, y = 1

"""
    Словари
"""
empty_dict = {}  # Задать словарь по-питоновски
empty_dict2 = dict()  # Не совсем по-питоновски
grades = {"Joel": 80, "Tim": 95}  # Литерал словаря

joels_grade = grades["Joel"]  # = 80

try:
    kates_grade = grades["Kate"]
except KeyError:
    print("Оценки для Kate отсутствуют!")

joel_has_grade = "Joel" in grades  # True
kate_has_grade = "Kate" in grades  # False

joels_grade = grades.get("Joel", 0)  # = 80
kates_grade = grades.get("Kate", 0)  # = 0
no_ones_grade = grades.get("No One")  # значение по умолчанию = None

grades["Tim"] = 99  # заменяет старое значение
grades["Kate"] = 100  # добавляет третью запись
num_students = len(grades)  # = 3

tweet = {
    "user": "joelgrus",
    "text": "Наука о данных - потрясающая тема",
    "retweet_count": 100,
    "hashtags": ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

tweet_keys = tweet.keys()  # список ключей
tweet_values = tweet.values()  # список значений
tweet_items = tweet.items()  # список кортежей (ключ, значение)

"user" in tweet_keys  # True, но использует медленное in списка
"user" in tweet  # по-питоновски, использует быстрое in словаря
"joelgrus" in tweet_values  # True

"""
    Словарь defaultdict
"""

document = ["data", "science", "from", "scratch"]

# Частотности слов
word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

word_counts = {}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1

word_counts = {}
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1

from collections import defaultdict

word_counts = defaultdict(int)  # int() возвращает 0
for word in document:
    word_counts[word] += 1

dd_list = defaultdict(list)  # list() возвращает пустой список
dd_list[2].append(1)  # теперь dd_list содержит {2: [1]}

dd_dict = defaultdict(dict)  # dict() возвращает пустой словарь dict
dd_dict["Joel"]["City"] = "Seattle"  # {"Joel" : {"City": Seattle"}}

dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1  # теперь dd_pair содержит {2: [0,1]}

"""
    Словарь Counter
"""

from collections import Counter

c = Counter([0, 1, 2, 0])  # в результате c = {0 : 2, 1 : 1, 2 : 1}

# Лучший вариант подсчета частотностей слов
word_counts = Counter(document)

# Напечатать 10 наиболее встречаемых слов и их частотность (встречаемость)
for word, count in word_counts.most_common(10):
    print(word, count)

primes_below_10 = {2, 3, 5, 7}

"""
    Множества
"""

s = set()  # Задать пустое множество
s.add(1)  # s = {1}
s.add(2)  # s = {1, 2}
s.add(2)  # s = {1, 2}
x = len(s)  # = 2
y = 2 in s  # = True
z = 3 in s  # = False

hundreds_of_other_words = []

# Список стоп-слов
stopwords_list = ["a", "an", "at"] + hundreds_of_other_words + ["yet", "you"]
"zip" in stopwords_list  # False, но проверяется каждый элемент

# Множество стоп-слов
stopwords_set = set(stopwords_list)
"zip" in stopwords_set  # очень быстрая проверка

item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list)  # 6
item_set = set(item_list)  # {1, 2, 3}
num_distinct_items = len(item_set)  # 3
distinct_item_list = list(item_set)  # [1, 2, 3]

"""
    Управляющие конструкции
"""

if 1 > 2:
    message = "Если 1 была бы больше 2..."
elif 1 > 3:
    message = "elif означает 'else if'"
else:
    message = "Когда все предыдущие условия не выполняются, используется else"

parity = "Четное" if x % 2 == 0 else "Нечетное"

x = 0
while x < 10:
    print(f"{x} меньше 10")
    x += 1

for x in range(10):
    print(f"{x} меньше 10")

for x in range(10):
    if x == 3:
        continue  # перейти сразу к следующей итерации
    if x == 5:
        break  # выйти из цикла
    print(x)

"""
    Истинность
"""

one_is_less_than_two = 1 < 2  # = True
true_equals_false = True == False  # = False

x = None


def some_function_that_returns_a_string():  # возвращает строковое значение
    return ""


s = some_function_that_returns_a_string()
if s:
    first_char = s[0]
else:
    first_char = ""

first_char = s and s[0]

safe_x = x or 0

safe_x = x if x is not None else 0

all([True, 1, {3}])  # True
all([True, 1, {}])  # False, {} = ложное
any([True, 1, {}])  # True, True = истинное
all([])  # True, ложные элементы в списке отсутствуют
any([])  # False, истинные элементы в списке отсутствуют

"""
    Сортировка
"""

x = [4, 1, 2, 3]
y = sorted(x)  # после сортировки = [1, 2, 3, 4], x не изменился
x.sort()  # теперь x = [1, 2, 3, 4]

# Сортировать список по абсолютному значению в убывающем порядке
x = sorted([-4, 1, -2, 3], key=abs, reverse=True)  # is [-4, 3, -2, 1]

# Сортировать слова и их частотности по убывающему значению частот
wc = sorted(word_counts.items(),
            key=lambda word_and_count: word_and_count[1],
            reverse=True)

"""
    Генераторы последовательностей
"""

# Четные числа
even_numbers = [x for x in range(5) if x % 2 == 0]  # [0, 2, 4]
# Квадраты чисел
squares = [x * x for x in range(5)]  # [0, 1, 4, 9, 16]
# Квадраты четных чисел
even_squares = [x * x for x in even_numbers]  # [0, 4, 16]

# Словарь с квадратами чисел
square_dict = {x: x * x for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
# Множество с квадратами чисел
square_set = {x * x for x in [1, -1]}  # {1}

# Нули
zeros = [0 for _ in even_numbers]  # Имеет ту же длину, что и even_numbers

# Пары
pairs = [(x, y)
         for x in range(10)
         for y in range(10)]  # 100 пар (0,0) (0,1)... (9,8), (9,9)

# Пары с возрастающим значением
increasing_pairs = [(x, y)  # только пары с x < y,
                    for x in range(10)  # range(мин, макс) равен
                    for y in range(x + 1, 10)]  # [мин, мин+1, ..., макс-1]

"""
    Функции-генераторы и генераторные выражения
"""


def lazy_range(n):
    i = 0
    while i < n:
        yield i
        i += 1


for i in lazy_range(10):
    print(f"i: {i}")


def natural_numbers():
    n = 1
    while True:
        yield n
        n += 1


lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)

"""
    Случайные числа
"""

import random

# Четыре равномерные случайные величины
four_uniform_randoms = [random.random() for _ in range(4)]

# [0.5714025946899135,      random.random() производит числа
#  0.4288890546751146,      равномерно в интервале между 0 и 1
#  0.5780913011344704,      функция random будет применяться
#  0.20609823213950174]     наиболее часто

random.seed(10)  # Задать случайную последовательность, установив в 10
print(random.random())  # 0.57140259469
random.seed(10)  # Переустановить seed в 10
print(random.random())  # 0.57140259469 опять

random.randrange(10)  # произвольно выбрать из range(10) = [0, 1, ..., 9]
random.randrange(3, 6)  # произвольно выбрать из range(3,6) = [3, 4, 5]

up_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(up_to_ten)
print(up_to_ten)
# [7, 2, 6, 8, 9, 4, 10, 1, 3, 5]

my_best_friend = random.choice(["Alice", "Bob", "Charlie"])  # "Bob" for me

# Лотерейные номера
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)  # [16, 36, 10, 6, 25, 9]

four_with_replacement = [random.choice(range(10)) for _ in range(4)]
print(four_with_replacement)  # [9, 4, 4, 2]

"""
    Регулярные выражения
"""

import re

re_examples = [
    not re.match("a", "cat"),
    re.search("a", "cat"),
    not re.search("c", "dog"),
    3 == len(re.split("[ab]", "carbs")),
    "R-D-" == re.sub("[0-9]", "-", "R2D2")
]

"""
    Объектно-ориентированное программирование
"""


# по традиции классам назначают имена с заглавной буквы
class Set:
    # ниже идут компонентные функции
    # каждая берет первый параметр "self" (еще одно правило),
    # который ссылается на конкретный используемый объект класса Set
    def __init__(self, values=None):
        self.dict = {}  # каждый экземпляр имеет собственное свойство dict,
        # которое используется для проверки
        # на принадлежность элементов множеству
        if values is not None:
            for value in values: self.add(value)

    def __repr__(self):
        """Это строковое представление объекта Set,
        которое выводится в оболочке или передается в функцию str()"""
        return "Set: " + str(self.dict.keys())
        # принадлежность представлена ключом в словаре self.dict
        # со значением True

    def add(self, value):
        self.dict[value] = True
        # значение принадлежит множеству, если его ключ имеется в словаре

    def contains(self, value):
        return value in self.dict

    def remove(self, value):
        del self.dict[value]


s = Set([1, 2, 3])
s.add(4)
print(s.contains(4))  # True
s.remove(3)
print(s.contains(3))  # False

"""
    Инструменты функционального программирования
"""


# возведение в степень power
def exp(base, power):
    return base ** power


# двойка в степени power
def two_to_the(power):
    return exp(2, power)


from functools import partial

# возвращает функцию с частичным приложением аргументов
two_to_the = partial(exp, 2)  # теперь это функция одной переменной
print(two_to_the(3))  # 8

square_of = partial(exp, power=2)  # квадрат числа
print(square_of(3))  # 9


def double(x):
    return 2 * x


xs = [1, 2, 3, 4]
twice_xs = [double(x) for x in xs]  # [2, 4, 6, 8]
twice_xs = map(double, xs)  # то же, что и выше
list_doubler = partial(map, double)  # удвоитель списка
twice_xs = list_doubler(xs)  # снова [2, 4, 6, 8]


# перемножить аргументы
def multiply(x, y):
    return x * y


products = map(multiply, [1, 2], [4, 5])  # [1 * 4, 2 * 5] = [4, 10]


# проверка четности
def is_even(x):
    """True, если x – четное; False, если x - нечетное"""
    return x % 2 == 0


x_evens = [x for x in xs if is_even(x)]  # список четных чисел = [2, 4]
x_evens = filter(is_even, xs)  # то же, что и выше
list_evener = partial(filter, is_even)  # функция, которая фильтрует
# список
x_evens = list_evener(xs)  # снова [2, 4]

from functools import reduce

x_product = reduce(multiply, xs)  # = 1 * 2 * 3 * 4 = 24
list_product = partial(reduce, multiply)  # функция, которая упрощает
# список
x_product = list_product(xs)  # снова = 24

"""
    Функция enumerate
"""

# список неких документов; здесь он пустой
documents = ["Лаба 1", "Лаба 2", "Лаба 3", "Лаба 4"]

# не по-питоновски
for i in range(len(documents)):
    print(f"Документ {i} - {documents[i]}")

# тоже не по-питоновски
i = 0
for document in documents:
    print(f"Документ {i} - {documents[i]}")
    i += 1

# Pythonic
for i, document in enumerate(documents):
    print(f"Документ {i} - {documents}")

"""
    Функция zip и распаковка аргументов
"""

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
[pair for pair in zip(list1, list2)]  # [('a', 1), ('b', 2), ('c', 3)]

pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)

letters, numbers = zip(('a', 1), ('b', 2), ('c', 3))


def add(a, b): return a + b


add(1, 2)  # вернёт 3
try:
    add([1, 2])
except TypeError:
    print("add ожидает два входных сигнала")
add(*[1, 2])  # вернёт 3

"""
    Переменные args и kwargs
"""


# Удвоитель
def doubler(f):
    def g(x):
        return 2 * f(x)

    return g


def f1(x):
    return x + 1


g = doubler(f1)
print(g(3))  # 8 или ( 3 + 1) * 2
print(g(-1))  # 0 или (-1 + 1) * 2


def f2(x, y):
    return x + y


g = doubler(f2)
try:
    g(1, 2)
except TypeError:
    print("Как определено, g принимает только один аргумент")


def magic(*args, **kwargs):
    print("Безымянные аргументы:", args)
    print("аргументы по ключу:", kwargs)


magic(1, 2, key="word", key2="word2")


# prints
#  unnamed args: (1, 2)
#  keyword args: {'key': 'word', 'key2': 'word2'}

def other_way_magic(x, y, z):
    return x + y + z


x_y_list = [1, 2]
z_dict = {"z": 3}
print(other_way_magic(*x_y_list, **z_dict))  # 6


# Корректный удвоитель
def doubler_correct(f):
    """Работает независимо от того, какого рода аргументы функция f ожидает"""

    def g(*args, **kwargs):
        """Какими бы ни были аргументы для g, передать их в f"""
        return 2 * f(*args, **kwargs)

    return g


g = doubler_correct(f2)
print(g(1, 2))  # 6
