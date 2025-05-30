import json
from bs4 import BeautifulSoup


def json_example():
    serialized = """{
        "title": "Data Science Book",
        "author": "Joel Grus",
        "publicationYear": 2014,
        "topics": ["data", "science", "data science"]
    }"""

    data = json.loads(serialized)

    print("Данные из JSON:")
    print(f"Название: {data['title']}")
    print(f"Автор: {data['author']}")
    print(f"Темы: {', '.join(data['topics'])}")

    if "data science" in data["topics"]:
        print("\nКнига относится к data science!")


# Пример работы с XML
def xml_example():
    xml_data = """
    <Book>
        <Title>Data Science Book</Title>
        <Author>Joel Grus</Author>
        <PublicationYear>2014</PublicationYear>
        <Topics>
            <Topic>data</Topic>
            <Topic>science</Topic>
            <Topic>data science</Topic>
        </Topics>
    </Book>
    """

    soup = BeautifulSoup(xml_data, 'xml')

    print("\nДанные из XML:")
    print(f"Название: {soup.Title.text}")
    print(f"Автор: {soup.Author.text}")

    topics = [topic.text for topic in soup.find_all('Topic')]
    print(f"Темы: {', '.join(topics)}")


if __name__ == "__main__":
    json_example()
    xml_example()
