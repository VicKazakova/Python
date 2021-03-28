class MyCheckListException(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
while True:
    number = (input('enter the number, for stop type "stop": '))
    if number == 'stop':
        break
    else:
        try:
            number = int(number)
        except (ValueError, MyCheckListException):
            print('this is not the number, enter the number: ')
        else:
            my_list.append(number)
print(my_list)
