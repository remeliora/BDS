from collections import Counter
import re
from time import sleep

import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


def is_video(td):
    """Check if it's a video by looking for pricelabel"""
    pricelabels = td('span', 'pricelabel')
    return (len(pricelabels) == 1 and
            pricelabels[0].text.strip().startswith("Video"))


def book_info(td):
    """Extract book details from td tag"""
    title = td.find("div", "thumbheader").a.text
    by_author = td.find('div', 'AuthorName').text
    authors = [x.strip() for x in re.sub("^By ", "", by_author).split(",")]
    isbn_link = td.find("div", "thumbheader").a.get("href")
    isbn = re.match("/product/(.*)\.do", isbn_link).groups()[0]
    date = td.find("span", "directorydate").text.strip()

    return {
        "title": title,
        "authors": authors,
        "isbn": isbn,
        "date": date
    }


def scrape(num_pages=2):
    """Scrape book data from O'Reilly website"""
    base_url = "https://shop.oreilly.com/category/browse-subjects/" + \
               "data.do?sortby=publicationDate&page="

    books = []

    for page_num in range(1, num_pages + 1):
        print("Processing page", page_num)
        try:
            url = base_url + str(page_num)
            soup = BeautifulSoup(requests.get(url).text, 'html.parser')

            for td in soup('td', 'thumbtext'):
                if not is_video(td):
                    books.append(book_info(td))

            sleep(1)  # Respectful delay between requests

        except Exception as e:
            print(f"Error processing page {page_num}: {e}")
            continue

    return books


def get_year(book):
    """Extract year from date string"""
    return int(book["date"].split()[1])


def plot_years(plt, books):
    """Plot book counts by year"""
    year_counts = Counter(get_year(book) for book in books)
    years = sorted(year_counts)
    book_counts = [year_counts[year] for year in years]

    plt.bar(years, book_counts)
    plt.xlabel("Year")
    plt.ylabel("# of Data Books")
    plt.title("Data Books Published by Year")
    plt.show()


if __name__ == "__main__":
    # Main execution
    books_data = scrape(num_pages=2)
    print(f"Collected data on {len(books_data)} books")

    if books_data:
        plot_years(plt, books_data)
    else:
        print("No book data was collected")