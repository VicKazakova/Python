from requests import get, utils
from datetime import date


def currency_rates(money):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    money_date = content.split('"')[5]
    day, month, year = money_date.split(".")
    dates = date(year=int(year), month=int(month), day=int(day))
    content = str(content).split('Valute ID=')
    for word in content:
        if money.upper() in word:
            currency = (word.replace('/', '').split("Value")[-2].replace('>', '').replace('<', '').replace(',', '.'))
            currency = float(currency)
            amount = str(word.split('Nominal')[-2].replace('>', '').replace('<', '').replace('/', ''))
            name = str(word.split('Name')[-2].replace('>', '').replace('<', '').replace('/', ''))
            final = f'По состоянию на {dates} {amount} {name}: {currency} рублей.'
            return final


if __name__ == '__main__':
    print(currency_rates('EUR'))
    print(currency_rates('AMD'))
    print(currency_rates('USD'))
