# наиболее распространенные слова (most_common_words.py)
# Для запуска из терминала:
# type the_bible.txt | python 1_3_most_common_words.py 3

# Результат: 6 the
#            3 dog
#            2 and
# Объяснение: В файле the_bible.txt слово "the" встречается 6 раз, "dog" - 3 раза и "and" - 2 раза.

import sys
from collections import Counter

if __name__ == "__main__":
    # передать число слов в качестве первого аргумента
    try:
        num_words = int(sys.argv[1])
    except:
        print("Применение: 1_3_most_common_words.py num_words")
        sys.exit(1)  # ненулевой код выхода сигнализирует об ошибке

    counter = Counter(word.lower()
                      for line in sys.stdin
                      for word in line.strip().split()
                      if word)

    for word, count in counter.most_common(num_words):
        sys.stdout.write(str(count))
        sys.stdout.write("\t")
        sys.stdout.write(word)
        sys.stdout.write("\n")
