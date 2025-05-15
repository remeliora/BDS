# Для запуска из терминала:
# python 2_2_count_hash_lines.py

import re

starts_with_hash = 0
with open('input.txt', 'r') as f:
    for line in f:
        if re.match("^#", line.strip()):
            starts_with_hash += 1

print(f"Строк с #: {starts_with_hash}")