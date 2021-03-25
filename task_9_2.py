class Road:
    __mass = 25
    __sm = 5

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def covering(self):
        total = int(self.__length * self.__width * (Road.__mass * 100) * (Road.__sm / 100) / 1000)
        print(f'На 1 метр необходимо {Road.__mass * 100}кг асфальта толщиной {Road.__sm}см')
        print(f'На дорогу шириной {user_width}м, длиной {user_length}м необходимо {total}т асфальта')


user_length = int(input('Введите длину дороги в метрах: '))
user_width = int(input('Введите ширину дороги в метрах: '))
road_Ordynka = Road(user_length, user_width)
road_Ordynka.covering()
