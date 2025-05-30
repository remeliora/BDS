from collections import Counter

import requests


class NewsAnalyzer:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2/"

    def get_news(self, query=None, country=None, category=None, page_size=20):
        """Универсальный метод для получения новостей"""
        url = f"{self.base_url}top-headlines"
        params = {'apiKey': self.api_key, 'pageSize': page_size}

        if query:
            params['q'] = query
        if country:
            params['country'] = country
        if category:
            params['category'] = category

        response = requests.get(url, params=params)
        return response.json()

    def analyze_news(self, query=None, category=None, country=None):
        """Анализ новостей с различными параметрами"""
        data = self.get_news(query=query, category=category, country=country)

        if data['status'] != 'ok':
            print(f"Ошибка: {data.get('message', 'Неизвестная ошибка')}")
            return

        articles = data['articles']

        if not articles:
            print("\nНовости не найдены. Попробуйте изменить параметры поиска.")
            return

        search_description = []
        if query:
            search_description.append(f"по запросу '{query}'")
        if category:
            search_description.append(f"в категории '{category}'")
        if country:
            search_description.append(f"для страны '{country}'")

        print(f"\nАнализ новостей {', '.join(search_description)}:")
        print(f"Найдено статей: {len(articles)}")

        sources = Counter(article['source']['name'] for article in articles)
        print("\nТоп источников:")
        for source, count in sources.most_common(5):
            print(f"  {source}: {count} статей")

        authors = Counter(article['author'] for article in articles if article['author'])
        if authors:
            print("\nТоп авторов:")
            for author, count in authors.most_common(5):
                print(f"  {author}: {count} статей")
        else:
            print("\nИнформация об авторах недоступна")

        dates = [article['publishedAt'][:10] for article in articles]
        date_counts = Counter(dates)
        print("\nДаты публикаций:")
        for date, count in date_counts.most_common():
            print(f"  {date}: {count} статей")

        print("\nПоследние новости:")
        for i, article in enumerate(articles[:5], 1):
            print(f"\n{i}. {article['title']}")
            if article['author']:
                print(f"   Автор: {article['author']}")
            print(f"   Источник: {article['source']['name']}")
            print(f"   Дата: {article['publishedAt']}")
            print(f"   Ссылка: {article['url']}")


def main():
    API_KEY = "f11e317fecab46eaa823a83163449a92"
    analyzer = NewsAnalyzer(API_KEY)

    print("=" * 50)
    print("Демонстрация работы с NewsAPI")
    print("=" * 50)

    print("\n1. Новости в категории 'наука'")
    analyzer.analyze_news(category="science")

    print("\n2. Новости об искусственном интеллекте")
    analyzer.analyze_news(query="artificial intelligence")

    print("\n3. Технологические новости в Великобритании")
    analyzer.analyze_news(category="technology", country="gb")


if __name__ == "__main__":
    main()
