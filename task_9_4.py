class Car:
    def __init__(self, s, c, n, is_p):
        self.speed = s
        self.color = c
        self.name = n
        self.ispolice = is_p

    def go(self):
        go = f'{self.name} is going'
        return go

    def stop(self):
        stop = f'{self.name} stopped'
        return stop

    def turn(self, direction):
        turn = f'{self.name} turned {direction}'
        return turn

    def show_speed(self):
        speed = f"{self.name}'s speed is {self.speed}"
        return speed


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            car_speed = f"{self.name}'s speed is {self.speed} -- too high!"
        else:
            car_speed = f"{self.name}'s speed is {self.speed}"
        return car_speed


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            car_speed = f"{self.name}'s speed is {self.speed} -- too high!"
        else:
            car_speed = f"{self.name}'s speed is {self.speed}"
        return car_speed


class PoliceCar(Car):
    pass


car_1 = TownCar(150, 'white', 'Zhiguli', False)
car_2 = SportCar(100, 'black', 'Lamborgini', False)
car_3 = WorkCar(45, 'grey', 'kamaz', False)
car_4 = PoliceCar(70, 'blue', 'police_car', True)
print(car_1.go())
print(car_2.go())
print(car_3.go())
print(car_4.go())
print(car_1.stop())
print(car_2.stop())
print(car_3.stop())
print(car_4.stop())
print(car_1.turn('left'))
print(car_2.turn('right'))
print(car_3.turn('right'))
print(car_4.turn('left'))
print(car_1.show_speed())
print(car_2.show_speed())
print(car_3.show_speed())
print(car_4.show_speed())
