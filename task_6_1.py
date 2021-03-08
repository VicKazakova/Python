with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
    content = ((i.split('-')[0], i.split('"')[1].split(' ')[0], i.split('"')[1].split(' ')[1]) for i in file)
    for j in content:
        print(j)
