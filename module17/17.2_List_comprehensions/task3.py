import random

def raise_price(price, percent):
    return round(price * (1 + percent/100), 2)

def sumsum(list):
    return round(sum(list), 2)

price_list = list(round(random.uniform(10, 99), 2) for _ in range(5))
first_prc = float(input('Процент на первый год: '))
second_prc = float(input('Процент на второй год: '))

price_first_year = list(raise_price(price, first_prc) for price in price_list)
price_sec_year = list(raise_price(price, second_prc) for price in price_first_year)

print(f'Сумма цен за каждый год: {sumsum(price_list)}; '
      f'{sumsum(price_first_year)}; {sumsum(price_sec_year)}')