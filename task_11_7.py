class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма z1 и z2 равна: z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Произведение z1 и z2 равно: z = ' \
               f'{self.a * other.a - self.b * other.b} + {self.a * other.b + self.b * other.a} * i'


a1 = int(input('Введите 1 число для комплексного числа 1: '))
a2 = int(input('Введите 2 число для комплексного числа 1: '))
b1 = int(input('Введите 1 число для комплексного числа 2: '))
b2 = int(input('Введите 2 число для комплексного числа 2: '))
z1 = Complex(a1, a2)
z2 = Complex(b1, b2)
print(z1 + z2)
print(z1 * z2)
