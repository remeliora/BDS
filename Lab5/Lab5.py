import re
from collections import Counter

import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

RAW_URL = (
    "https://raw.githubusercontent.com/"
    "remeliora/BDS/master/TestData/books.html"
)
DELAY_SECONDS = 30
OUTPUT_CSV = "oreilly_books.csv"


def is_video(td):
    """
    True, если внутри td ровно один <span class="pricelabel">,
    и его текст начинается с 'Video'
    """
    pricelabels = td.find_all('span', class_='pricelabel')
    return len(pricelabels) == 1 and pricelabels[0].text.strip().startswith("Video")


def book_info(td):
    """
    Из td<class="thumbtext"> вытаскивает dict с полями:
      - title  (название)
      - authors (список строк; если не найдено — пустой список)
      - isbn   (если в href встречается /product/XXX.do)
      - date   (текст из <span class="directorydate">)
      - price  (текст из <span class="price">)
    """
    # название
    title_tag = td.find("div", class_="thumbheader").find("a")
    title = title_tag.text.strip() if title_tag else ""

    # автора(ов)
    author_div = td.find("div", class_="AuthorName")
    if author_div:
        # Убираем внешнее "By " и делим по запятым
        authors = [x.strip() for x in re.sub(r"^By\s+", "",
                                             author_div.text).split(",")]
    else:
        authors = []

    # ISBN из ссылки вида "/product/978xxxxx.do"
    href = title_tag.get("href", "") if title_tag else ""
    m = re.match(r"/product/(.*)\.do", href)
    isbn = m.group(1) if m else ""

    # дата и цена
    date_tag = td.find("span", class_="directorydate")
    date = date_tag.text.strip() if date_tag else ""
    price_tag = td.find("span", class_="price")
    price = price_tag.text.strip() if price_tag else ""

    return {
        "title": title,
        "authors": authors,
        "isbn": isbn,
        "date": date,
        "price": price
    }


def get_year(book):
    """
    Из строки вида 'April 2023' возвращает 2023 (int).
    """
    parts = book["date"].split()
    try:
        return int(parts[-1])
    except:
        return None


def main():
    # 1) Скачиваем и парсим
    html = requests.get(RAW_URL).text
    soup = BeautifulSoup(html, 'html5lib')

    # 2) Находим все карточки
    tds = soup.find_all('td', class_='thumbtext')
    print(f"Всего <td class='thumbtext'> на странице: {len(tds)}")

    # 3) Фильтруем видео и собираем книги
    books = []
    for td in tds:
        if not is_video(td):
            books.append(book_info(td))
    print(f"Книг (Video отфильтрованы): {len(books)}")

    # 4) Сохраняем в CSV
    import csv
    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f,
                                fieldnames=["title", "authors", "isbn", "date", "price"])
        writer.writeheader()
        for bk in books:
            # authors — список, в CSV склеим через ';'
            bk_row = bk.copy()
            bk_row["authors"] = ";".join(bk_row["authors"])
            writer.writerow(bk_row)
    print(f"Результат записан в {OUTPUT_CSV}")

    # 5) Строим график числа книг по годам
    years = [get_year(bk) for bk in books if get_year(bk) is not None]
    year_counts = Counter(years)

    xs = sorted(year_counts)
    ys = [year_counts[x] for x in xs]

    plt.plot(xs, ys)
    plt.xlabel("Год")
    plt.ylabel("Число книг")
    plt.title("Публикации книг по данным — по годам")
    plt.grid(True)
    # plt.show()
    plt.savefig("График.png", dpi=150)
    print("График сохранён в График.png")


if __name__ == "__main__":
    main()
