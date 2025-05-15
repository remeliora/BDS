# Для запуска из терминала:
# python 2_5_write_csv.py

import csv

today_prices = {'AAPL': 90.91, 'MSFT': 41.68, 'FB': 64.5}

with open('comma_delimited_stock_prices.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(["Symbol", "Price"])
    for stock, price in today_prices.items():
        writer.writerow([stock, price])