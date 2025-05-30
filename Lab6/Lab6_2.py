import requests
import json
from collections import Counter
from dateutil.parser import parse


def get_github_repos(username):
    """Получаем информацию о репозиториях пользователя GitHub"""
    endpoint = f"https://api.github.com/users/{username}/repos"
    response = requests.get(endpoint)

    if response.status_code == 200:
        repos = json.loads(response.text)
        return repos
    else:
        print(f"Ошибка: {response.status_code}")
        return None


def analyze_repo_dates(repos):
    """Анализируем даты создания репозиториев"""
    dates = [parse(repo["created_at"]) for repo in repos]

    month_counts = Counter(date.month for date in dates)
    weekday_counts = Counter(date.weekday() for date in dates)

    print("\nСоздание репозиториев по месяцам:")
    for month, count in month_counts.most_common():
        print(f"{month:02d}: {count} репозиториев")

    print("\nСоздание репозиториев по дням недели:")
    weekdays = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
    for weekday, count in weekday_counts.most_common():
        print(f"{weekdays[weekday]}: {count} репозиториев")


def analyze_repo_languages(repos):
    """Анализируем языки программирования в репозиториях"""
    last_5_repos = sorted(repos, key=lambda r: r["created_at"], reverse=True)[:5]
    languages = [repo["language"] for repo in last_5_repos if repo["language"]]

    print("\nЯзыки в последних 5 репозиториях:")
    for lang in languages:
        print(f"- {lang}")


if __name__ == "__main__":
    username = "remeliora"
    repos = get_github_repos(username)

    if repos:
        print(f"Найдено {len(repos)} репозиториев пользователя {username}")
        analyze_repo_dates(repos)
        analyze_repo_languages(repos)
