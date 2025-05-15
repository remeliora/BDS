# egrep.py
# Для запуска из терминала необходимо добавить аргумент
# Пример: python 1_1_egrep.py hello

import re
import sys

if __name__ == "__main__":
    # sys.argv - список аргументов командной строки
    # sys.argv[0] - имя самой программы
    # sys.argv[1] - регулярное выражение, указываемое в командной строке
    regex = sys.argv[1]

    # для каждой строки, переданной сценарию
    for line in sys.stdin:
        # если она соответствует регулярному выражению regex,
        # записать ее в stdout
        if re.search(regex, line):
            sys.stdout.write(line)
