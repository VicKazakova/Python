def type_logger(function):
    def wrapper(*args, **kwargs):
        n = [f'{function.__name__}({el}: {type(el)})' for el in args] + \
            [f'{function.__name__}({el}: {type(kwargs[el])})' for el in kwargs]
        print(*n)
    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


try:
    user_n = int(input('Enter the number: '))
    a = calc_cube(user_n)
except ValueError:
    print('wrong val')
