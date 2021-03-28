class MyZeroDivision(Exception):
    def __init__(self, txt):
        self.txt = txt


first = input('enter number 1: ')
second = input('enter number 2: ')


try:
    first = int(first)
    second = int(second)

    if second == 0:
        raise MyZeroDivision('enter something that is not zero')
except (ValueError, MyZeroDivision) as err:
    print(err)
else:
    print(first // second)
