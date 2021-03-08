from itertools import zip_longest
list_users = []
list_hobbies = []
with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobbies.csv', 'r', encoding='utf-8') as hobbies:
        for user in users:
            user = str(user.replace(',', ' ').replace('\n', '').replace('\ufeff', ''))
            list_users.append(user)
        for hobby in hobbies:
            hobby = str(hobby.replace('\n', ''))
            list_hobbies.append(hobby)
        result = zip_longest(list_users, list_hobbies, fillvalue=None)
        result = dict(result)
        with open('result.txt', 'w', encoding='utf-8') as f:
            f.write(str(result))
