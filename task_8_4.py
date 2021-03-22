def val_checker(l_func):
    def _val_checker(func):
        def wrapper(num):
            if l_func(num):
                print(func(num))
            else:
                raise ValueError('wrong num')
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


try:
    user_n = int(input('Enter the number: '))
    a = calc_cube(user_n)
except ValueError:
    print('wrong val')
