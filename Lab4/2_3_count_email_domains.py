# Для запуска из терминала:
# python 2_3_count_email_domains.py

from collections import Counter


def get_domain(email):
    return email.lower().split("@")[-1]


with open('email_addresses.txt', 'r') as f:
    domains = Counter(get_domain(line.strip()) for line in f if "@" in line)

print(domains.most_common())
