# Для запуска из терминала:
# python 2_1_read_file.py


# Открытие файла для чтения
with open('reading_file.txt', 'r') as f:
    data = f.read()  # Чтение всего содержимого

# Открытие файла для записи (перезаписывает существующий)
with open('writing_file.txt', 'w') as f:
    f.write("Hello, World!\n")

# Открытие файла для добавления в конец
with open('appending_file.txt', 'a') as f:
    f.write("New line\n")
