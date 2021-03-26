from abc import abstractmethod, ABC


class Clothes(ABC):
    result = 0

    def __init__(self, i):
        self.i = i

    @property
    @abstractmethod
    def clothes_size(self):
        pass

    def __add__(self, other):
        Clothes.result += self.clothes_size + other.clothes_size
        return Costume(0)

    def __str__(self):
        result = Clothes.result
        Clothes.result = 0
        return f'{result}'


class Coat(Clothes):
    @property
    def clothes_size(self):
        return round(self.i / 6.5) + 0.5


class Costume(Clothes):
    @property
    def clothes_size(self):
        return round((2 * self.i + 0.3) / 100)


v = int(input('insert the size of the coat: '))
h = int(input('insert the height for the costume (in cm): '))
coat_1 = Coat(v)
costume_1 = Costume(h)
print(f'required material length for the size {v} coat and for the costume with {h} height is: {coat_1 + costume_1} m')
