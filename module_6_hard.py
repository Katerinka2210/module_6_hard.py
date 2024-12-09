import math
class Figure:
    sides_count = 0 # количество сторон
    def __init__(self, color, sides, filled = False): # список сторон и список цветов, закрашенный, изначально не закрашенный
        self.__sides = sides  # список сторон (целые числа), __ - инкапсулироваые атрибуты
        self.__color = color  # список цветов в форматре RGb
        self.filled = filled # если цвет задается, то считывается как закрашенный

    def get_color(self): # получение цвета
        return self.__color

    def __is_valid_color(self, r, g, b): # проверить допустимость цвета
        for i in [r, g, b]:
            if isinstance(i, int) and 0 <= i <= 255:
                return True
            return False

    def set_color(self, r, g, b):  # метод, устанавливающий цвет
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides): # метод допустимых сторон
        if len(sides) == self.sides_count: # если количество сторон равно количеству сторон определенной фигуры, то
            for i in sides:
                if isinstance(i, int) and i > 0:
                    return True
                return False

    def get_sides(self):
        return self.__sides

    def __len__(self): # возвращает периметр фигуры
        return sum(self.__sides)

    def set_sides(self, *new_sides): # метод принимает новые стороны и если их кол-во не равно sides_count, то не
        if self.__is_valid_sides(*new_sides): # изменять, в противном случае менять
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1
    def __init__(self, color, *sides):
        super().__init__(color, sides)
        self.__radius = sides[0]  # радиус окружности

    def get_square(self):
        return math.pi * (self.__radius ** 2)  # площадь круга


class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        p = sum(self.get_sides()) / 2
        s1 = math.sqrt(p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2]))
        return s1

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_length):
        super().__init__(color, [side_length] * self.sides_count)  # передаем одинаковые стороны
        self.__side_length = side_length

    def get_volume(self):
        return self.__side_length ** 3  # объем куба

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
