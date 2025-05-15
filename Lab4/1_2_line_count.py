# подсчет строк (line_count.py)
# Для запуска из терминала:
# type numbers.txt | python 1_1_egrep.py "[0-9]" | python 1_2_line_count.py

# Результат: 3
# Объяснение: Скрипт 1_1_egrep.py находит 3 строки с числами (123, 45, 678) из файла numbers.txt,
# а 1_2_line_count.py подсчитывает их.

import sys

if __name__ == "__main__":

    count = 0
    for line in sys.stdin:
        count += 1

    # результат выводится на консоль sys.stdout
    print(count)
