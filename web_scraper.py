import requests
from bs4 import BeautifulSoup

K = 1000


def get_prices_per_program():
    url = 'https://www.e-milhas.com/cotacao'
    req = requests.get(url)
    content = BeautifulSoup(req.content, 'html.parser')

    price_table = content.table.tbody
    rows = price_table.find_all('tr')

    prices_per_program = {}
    program_name = rows[0].th.string
    for row in rows:
        if row.th is not None:
            program_name = row.th.string
            if prices_per_program.get(program_name) is None:
                prices_per_program[program_name] = {}
        mile_range, price = list(map(lambda td: td.string, row.find_all('td')))
        start, end = mile_range.split('à')
        start = int(''.join([char for char in start if char.isnumeric()]))
        end = int(''.join([char for char in end if char.isnumeric()]))
        mile_range = range(start * K, (end * K) + 1)
        price = float(price.replace('R$', '').replace(',', '.'))
        prices_per_program[program_name][mile_range] = price
    return prices_per_program
