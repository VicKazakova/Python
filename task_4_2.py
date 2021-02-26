from requests import get, utils


def currency_rates(money):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    content = str(content).split('Valute ID=')
    for word in content:
        if money.upper() in word:
            currency = (word.split("Value")[-2].replace('>', '').replace('<', '').replace(',', '.').replace('/', ''))
            currency = float(currency)
            amount = str(word.split('Nominal')[-2].replace('>', '').replace('<', '').replace('/', ''))
            name = str(word.split('Name')[-2].replace('>', '').replace('<', '').replace('/', ''))
            final = f'{amount} {name}: {currency} рублей.'
            return final


print(currency_rates('EUR'))
print(currency_rates('AMD'))
print(currency_rates('USD'))
