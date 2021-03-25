class Worker:
    name = 'Boris'
    surname = 'Korotkin'
    position = 'janitor'
    money = {"wage": 10000, "bonus": 20000}
    _income = money['wage'] + money['bonus']


class Position(Worker):
    def get_full_name(self):
        full_name = f'Employee name: {Worker.name} {Worker.surname}'
        print(full_name)

    def get_total_income(self):
        full_income = f'His total income: {Worker._income}'
        print(full_income)


employee_1 = Position()
employee_1.get_full_name()
employee_1.get_total_income()
