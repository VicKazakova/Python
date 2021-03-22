import re


def email_parse(address):
    re_username = re.compile(r'^\w+\@[a-z]+\.[a-z]+$')
    email_address = str(re_username.findall(address))
    try:
        username = re.split(r'@', email_address)[0].split("'")[1]
        domain = f'''@{re.split(r"@", email_address)[1].split("'")[0]}'''
        final_dict = dict([(username, domain)])
    except IndexError:
        print('wrong email, try again')
    else:
        return final_dict


email = input('Введите email: ')
print(email_parse(email.lower()))
