# Для запуска из терминала:
# python 2_4_read_csv.py

import csv

with open('tab_delimited_stock_prices.txt', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        date, symbol, price = row
        print(f"{date}: {symbol} — ${price}")