from itertools import zip_longest
from sys import argv
u, h, final_f = argv[1:]
list_users = []
list_hobbies = []
with open(u, 'r', encoding='utf-8') as users:
    with open(h, 'r', encoding='utf-8') as hobbies:
        for user in u:
            user = str(user.replace('\n', '').replace('\ufeff', ''))
            list_users.append(user)
        for hobby in h:
            hobby = str(hobby.replace('\n', ''))
            list_hobbies.append(hobby)
        result = zip_longest(list_users, list_hobbies, fillvalue=None)
        with open(final_f, 'w', encoding='utf-8') as f:
            for i in result:
                print(f'{i[0]}: {i[1]}', file=f)
