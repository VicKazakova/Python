class Stationery:
    def __init__(self, t):
        self.title = t

    def draw(self):
        drawing = 'Запуск отрисовки'
        return drawing


class Pen(Stationery):
    def draw(self):
        drawing = f'Запуск отрисовки с помощью инструмента {self.title}'
        return drawing


class Pencil(Stationery):
    def draw(self):
        drawing = f'Запуск отрисовки с помощью инструмента {self.title}'
        return drawing


class Handle(Stationery):
    def draw(self):
        drawing = f'Запуск отрисовки с помощью инструмента {self.title}'
        return drawing


drawing_1 = Pen('ручка')
drawing_2 = Pencil('карандаш')
drawing_3 = Handle('маркер')
print(drawing_1.draw())
print(drawing_2.draw())
print(drawing_3.draw())
