class Cell:

    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'{self.number}'

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if self.number - other.number > 0:
            return Cell(self.number - other.number)
        else:
            message = 'Ячеек в первой клетке меньше, чем во второй'
            return message

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __floordiv__(self, other):
        return Cell(self.number // other.number)

    def make_order(self, rows):
        order = '\n'.join(['*' * rows for _ in range(self.number // rows)]) + '\n' + '*' * (self.number % rows)
        return order


cells_1 = int(input('Введите количество клеток 1: '))
cells_2 = int(input('Введите количество клеток 2: '))
cell_1 = Cell(cells_1)
cell_2 = Cell(cells_2)
print(f'Сумма клеток: {cell_1 + cell_2}')
print(f'Разновсть клеток: {cell_1 - cell_2}')
print(f'Произведение клеток: {cell_1 * cell_2}')
print(f'Деление клеток: {cell_1 // cell_2}')
print(f'Упорядочить 1: {cell_1.make_order(15)}')
print(f'Упорядочить 2: {cell_2.make_order(45)}')
