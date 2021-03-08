from itertools import zip_longest
list_users = []
list_hobbies = []
with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobbies.csv', 'r', encoding='utf-8') as hobbies:
        for user in users:
            user = str(user.replace('\n', '').replace('\ufeff', ''))
            list_users.append(user)
        for hobby in hobbies:
            hobby = str(hobby.replace('\n', ''))
            list_hobbies.append(hobby)
        result = zip_longest(list_users, list_hobbies, fillvalue=None)
        with open('users_hobby.txt', 'w', encoding='utf-8') as f:
            for i in result:
                print(f'{i[0]}: {i[1]}', file=f)
