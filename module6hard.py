from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, color, *sides, filled=True):
        self.__sides = list(sides)
        self.__color = list(color)
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, color):
        for i in color:
            if not (-1 < i < 256):
                return False
        return True

    def set_color(self, *color):
        if self.__is_valid_color(color):
            self.__color = list(color)

    def __is_valid_sides(self, *sides):
        if len(sides) != len(self.__sides):
            return False
        for side in sides:
            if not isinstance(side, int) and side > 0:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides, **kwargs):
        if len(sides) != self.sides_count:
            sides = [1]
        super().__init__(color, *sides, **kwargs)
        self._radius = sides[0] / (2 * pi)

    def get_square(self):
        return pi * self._radius**2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides, **kwargs):
        if len(sides) != self.sides_count:
            sides = [1 for _ in range(self.sides_count)]
        super().__init__(color, *sides, **kwargs)
        a, b, c = sides
        p = (a + b + c) / 2
        self._height = 2 * sqrt(p * (p - a) * (p - b) * (p - c)) / a

    def get_square(self):
        a, *_ = self.get_sides()
        return a * self._height / 2


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides, **kwargs):
        if len(sides) == 1:
            sides = [sides[0] for _ in range(self.sides_count)]
        elif len(sides) != self.sides_count:
            sides = [1 for _ in range(self.sides_count)]
        super().__init__(color, *sides, **kwargs)

    def get_volume(self):
        x = self.get_sides()
        return x[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())


# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# results:
# [55, 66, 77]
# [222, 35, 130]
# [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
# [15]
# 15
# 216

# more tests
circle2 = Circle((200, 200, 100), 10, 15, 6)
# , т.к. сторона у круга всего 1, то его стороны будут - [1]
assert circle2.get_sides() == [1]
# , т.к. площадь круга, число с типа float а их лучше сравнивать через вхождение
assert 0.0794 < circle2.get_square()
assert 0.0796 > circle2.get_square()
# Проверка периметра круга, это и есть длина:
assert len(circle2) == 1

triangle2 = Triangle((200, 200, 100), 10, 6)
# , т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
assert triangle2.get_sides() == [1, 1, 1]
# , т.к. площадь триугольника, число с типа float а их лучше сравнивать через вхождение
assert 0.4330 < triangle2.get_square()
assert 0.4331 > triangle2.get_square()
# Проверка периметра треугольника, это и есть длина:
assert len(triangle2) == 3


cube2 = Cube((200, 200, 100), 9)
# , т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
assert cube2.get_sides() == [9 for _ in range(12)]

cube3 = Cube((200, 200, 100), 9, 12)
# , т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]
assert cube3.get_sides() == [1 for _ in range(12)]
# Проверка периметра куба, это и есть длина:
assert len(cube3) == 12

# , приминение новой длинны сторон
cube3.set_sides(9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9)
assert cube3.get_sides() == [9 for _ in range(12)]
