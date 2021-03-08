result = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
    content = (i.split(' ')[0] for i in file)
    for j in content:
        if j in result:
            result[j] = result[j] + 1
        else:
            result[j] = 1
quantity = max(result.values())
spammer = list(result.keys())[list(result.values()).index(quantity)]
print(f'Спаммер {spammer}, кол-во запросов: {quantity}')



