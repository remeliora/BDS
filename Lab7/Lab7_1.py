import csv
from collections import defaultdict
from functools import reduce

import dateutil.parser


# Функции для очистки и форматирования данных
def try_or_none(f):
    def f_or_none(x):
        try:
            return f(x)
        except:
            return None

    return f_or_none


def parse_row(input_row, parsers):
    return [try_or_none(parser)(value) if parser is not None else value
            for value, parser in zip(input_row, parsers)]


def parse_rows_with(reader, parsers):
    for row in reader:
        yield parse_row(row, parsers)


def picker(field_name):
    return lambda row: row[field_name]


def pluck(field_name, rows):
    return map(picker(field_name), rows)


def group_by(grouper, rows, value_transform=None):
    grouped = defaultdict(list)
    for row in rows:
        grouped[grouper(row)].append(row)

    if value_transform is None:
        return grouped
    else:
        return {key: value_transform(rows)
                for key, rows in grouped.items()}


def percent_price_change(yesterday, today):
    return today["closing_price"] / yesterday["closing_price"] - 1


def day_over_day_changes(grouped_rows):
    ordered = sorted(grouped_rows, key=picker("date"))
    return [{"symbol": today["symbol"],
             "date": today["date"],
             "change": percent_price_change(yesterday, today)}
            for yesterday, today in zip(ordered, ordered[1:])]


def combine_pct_changes(pct_change1, pct_change2):
    return (1 + pct_change1) * (1 + pct_change2) - 1


def overall_change(changes):
    return reduce(combine_pct_changes, pluck("change", changes))


def load_stock_data(filename):
    data = []
    with open(filename, mode='r') as f:
        reader = csv.reader(f)
        for line in parse_rows_with(reader, [dateutil.parser.parse, None, float]):
            # Преобразуем в словарь и добавляем только строки без ошибок
            if len(line) == 3 and None not in line:
                data.append({
                    'date': line[0],
                    'symbol': line[1],
                    'closing_price': line[2]
                })
            else:
                print(f"Пропущена строка с ошибкой: {line}")
    return data


# Основной анализ
def analyze_stock_data(data):
    print("\nАнализ данных об акциях:")

    # 1. Максимальные цены по акциям
    max_prices = group_by(picker("symbol"), data,
                          lambda rows: max(pluck("closing_price", rows)))
    print("\nМаксимальные цены по акциям:")
    for symbol, price in max_prices.items():
        print(f"{symbol}: {price:.2f}")

    # 2. Дневные изменения цен
    changes_by_symbol = group_by(picker("symbol"), data, day_over_day_changes)
    all_changes = [change
                   for changes in changes_by_symbol.values()
                   for change in changes]

    if not all_changes:
        print("\nНедостаточно данных для анализа дневных изменений")
        return

    # 3. Максимальное и минимальное дневное изменение
    max_change = max(all_changes, key=picker("change"))
    min_change = min(all_changes, key=picker("change"))

    print("\nМаксимальное дневное изменение:")
    print(f"{max_change['symbol']} {max_change['date'].strftime('%Y-%m-%d')}: {max_change['change']:.2%}")

    print("\nМинимальное дневное изменение:")
    print(f"{min_change['symbol']} {min_change['date'].strftime('%Y-%m-%d')}: {min_change['change']:.2%}")

    # 4. Помесячные изменения
    overall_change_by_month = group_by(lambda row: row['date'].month,
                                       all_changes,
                                       overall_change)

    print("\nСуммарные помесячные изменения:")
    for month, change in sorted(overall_change_by_month.items()):
        print(f"{month:02d}: {change:.2%}")


if __name__ == "__main__":
    # Загрузка данных
    filename = "comma_delimited_stock_prices.csv"
    print(f"Загрузка данных из файла {filename}...")
    stock_data = load_stock_data(filename)

    # Проверка загруженных данных
    print(f"\nЗагружено {len(stock_data)} записей:")
    for i, row in enumerate(stock_data[:6]):
        print(row)

    # Анализ данных
    analyze_stock_data(stock_data)
