class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def method_1(cls, date):
        try:
            d, m, y = map(int, date.split('-'))
        except ValueError as err:
            return err
        else:
            return d, m, y

    @staticmethod
    def method_2():
        a = []
        try:
            if 0 < Date(user_date).method_1(user_date)[0] < 31:
                a.append('date ok!')
            else:
                a.append('date is wrong')
            if 0 < Date(user_date).method_1(user_date)[1] < 13:
                a.append('month ok!')
            else:
                a.append('month is wrong')
            if 999 < Date(user_date).method_1(user_date)[2] < 9999:
                a.append('year ok!')
            else:
                a.append('year is wrong')
        except TypeError as err:
            return err
        else:
            return a


user_date = input('Enter the date in the following format: dd-mm-yyyy: ')
date_one = Date.method_1(user_date)
print(date_one)
print(Date.method_2())
