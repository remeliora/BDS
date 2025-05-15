# Для запуска из терминала:
# python 2_6_bad_csv.py

data = [
    ["test1", "success", "Monday"],
    ["test2", "success, kind of", "Tuesday"],
    ["test3", "failure, kind of", "Wednesday"]
]

with open('bad_csv.txt', 'w') as f:
    for row in data:
        f.write(",".join(row) + "\n")
