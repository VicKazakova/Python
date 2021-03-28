from abc import ABC, abstractmethod


class Warehouse:
    def __init__(self, name, price, supply):
        self.name = name
        self.price = price
        self.supply = supply

    def receive_tech(self, received_tech):
        with open('orgtech.txt', 'a', encoding='utf-8') as f:
            a_receive = f'Получено на склад {received_tech} шт техники: ' \
                        f'{self.name}, общая стоимость: {self.price * received_tech} руб, поставщик: {self.supply} \n'
            f.write(str(a_receive))

    def send_tech(self, sent_tech, dept):
        with open('orgtech.txt', 'a', encoding='utf-8') as f:
            a_sent = f'Отгружено со склада {sent_tech} шт техники: {self.name} в отдел: {dept} \n'
            f.write(str(a_sent))


class OrgTech(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def workload(self, workload):
        pass


class Printer(OrgTech):
    def workload(self, workload):
        with open('orgtech.txt', 'a', encoding='utf-8') as f:
            f.write(f'Напечатано {workload} листов, техника: {self.name} \n')


class Scanner(OrgTech):
    def workload(self, workload):
        with open('orgtech.txt', 'a', encoding='utf-8') as f:
            f.write(f'Отсканировано {workload} листов, техника: {self.name} \n')


class Xerox(OrgTech):
    def workload(self, workload):
        with open('orgtech.txt', 'a', encoding='utf-8') as f:
            f.write(f'Откопировано {workload} листов, техника: {self.name} \n')


printer_1 = Printer(input('Модель принтера 1: '))
scanner_1 = Scanner(input('Модель сканера 1: '))
xerox_1 = Xerox(input('Модель ксерокса 1: '))
printer_quan_1 = input('Цена за единицу модели принтера 1: ')
scan_quan_1 = input('Цена за единицу модели сканера 1: ')
xerox_quan_1 = input('Цена за единицу модели ксерокса 1: ')
try:
    printer_quan_1 = (int(printer_quan_1))
    scan_quan_1 = (int(scan_quan_1))
    xerox_quan_1 = (int(xerox_quan_1))
except ValueError as err:
    print(err)
else:
    pass
printer_supply_1 = (input('Поставщик принтера 1: '))
scan_supply_1 = (input('Поставщик сканера 1: '))
xerox_supply_1 = (input('Поставщик ксерокса 1: '))

printer_1_w = Warehouse(printer_1.name, printer_quan_1, printer_supply_1)
scanner_1_w = Warehouse(scanner_1.name, scan_quan_1, scan_supply_1)
xerox_1_w = Warehouse(xerox_1.name, xerox_quan_1, xerox_supply_1)


# Запись о получении техники на склад:
pr_quan = input(f'Кол-во принтеров {printer_1_w.name}, отгруженных на склад: ')
sc_quan = input(f'Кол-во принтеров {scanner_1_w.name}, отгруженных на склад: ')
xer_quan = input(f'Кол-во принтеров {xerox_1_w.name}, отгруженных на склад: ')
try:
    pr_quan = int(pr_quan)
    sc_quan = int(sc_quan)
    xer_quan = int(xer_quan)
except ValueError as err:
    print(err)
else:
    Warehouse(printer_1_w.name, printer_1_w.price, printer_1_w.supply).receive_tech(pr_quan)
    Warehouse(scanner_1_w.name, scanner_1_w.price, scanner_1_w.supply).receive_tech(sc_quan)
    Warehouse(xerox_1_w.name, xerox_1_w.price, scanner_1_w.supply).receive_tech(xer_quan)

# Запись об отгрузке техники:
pr_quan_sent = input(f'Кол-во принтеров {printer_1_w.name}, отгруженных со склада: ')
sc_quan_sent = input(f'Кол-во принтеров {scanner_1_w.name}, отгруженных со склада: ')
xer_quan_sent = input(f'Кол-во принтеров {xerox_1_w.name}, отгруженных со склада: ')
try:
    pr_quan_sent = int(pr_quan_sent)
    sc_quan_sent = int(sc_quan_sent)
    xer_quan_sent = int(xer_quan_sent)
except ValueError as err:
    print(err)
else:
    Warehouse(printer_1_w.name, printer_1_w.price, printer_1_w.supply).send_tech(pr_quan_sent, 'HR')
    Warehouse(scanner_1_w.name, scanner_1_w.price, scanner_1_w.supply).send_tech(sc_quan_sent, 'Finance Dept')
    Warehouse(xerox_1_w.name, xerox_1_w.price, scanner_1_w.supply).send_tech(xer_quan_sent, 'Accounting Office')
# Запись об использовании техники:
pr_workload = input(f'Кол-во напечатанных листов на технике: {printer_1.name}: ')
sc_workload = input(f'Кол-во напечатанных листов на технике: {printer_1.name}: ')
xer_workload = input(f'Кол-во напечатанных листов на технике: {printer_1.name}: ')
try:
    pr_workload = int(pr_workload)
    sc_workload = int(sc_workload)
    xer_workload = int(xer_workload)
except ValueError as err:
    print(err)
else:
    Printer(printer_1.name).workload(pr_workload)
    Scanner(scanner_1.name).workload(sc_workload)
    Xerox(xerox_1.name).workload(xer_workload)
