import re
from itertools import zip_longest


ip_list = []
requests_list = []
codes_list = []
size_list = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    content = str(f.read())
    remote_addr = re.findall(r'\w.+ [-] [-]', content)
    for ip in remote_addr:
        ip = ip.split(' ')[0]
        ip_list.append(ip)
    # print(len(ip_list)) -- чтобы сверить кол-во элементов
    request_datetime = re.findall(r'\d{2}[/]\w+[/]\d{4}[:]\d{2}[:]\d{2}[:]\d{2} [+]\d{4}', content)
    # print(len(request_datetime)) -- чтобы сверить кол-во элементов
    request_type = re.findall(r'["][A-Z]+ [/]', content)
    for request in request_type:
        request = request.split(' ')[0][1:]
        requests_list.append(request)
    # print(len(requests_list)) -- чтобы сверить кол-во элементов
    requested_resource = re.findall(r'[/][a-z]+[/][a-z]+[_][0-9]', content)
    # print(len(requested_resource)) -- чтобы сверить кол-во элементов
    response_code = re.findall(r'["] [0-9]{3}', content)
    for code in response_code:
        code = code.split(' ')[-1]
        codes_list.append(code)
    # print(len(codes_list)) -- чтобы сверить кол-во элементов
    response_size = re.findall(r' [0-9]+ ["]', content)
    for size in response_size:
        size = size.split(' ')[1]
        size_list.append(size)
    # print(len(size_list)) -- чтобы сверить кол-во элементов
final_parse = \
    zip_longest(ip_list, request_datetime, requests_list, requested_resource, codes_list, size_list, fillvalue='None')
print(next(final_parse))
print(next(final_parse))
print(next(final_parse))
