from math import sqrt


class Figure:
    sides_count = 0

    def __init__(self, rgb, *sides):
        self.__sides = []  # список сторон int
        self.__color = []  # список цветов RGB
        filled = False  # заливка
        self.set_color(*rgb)

        self.__sides_len = 1  # длина сторон если кол-во сторон не соответствует фигуре
        if self.__is_valid_sides(*sides):
            self.__sides = [*sides]
        else:
            if (len(sides) == 1) and (sides[0] > 0):
                self.__sides_len = sides[0]  # длина сторон если передан один положительный размер
            for i in range(self.sides_count):
                self.__sides.append(self.__sides_len)

    def __is_valid_color(self, r, g, b):
        if (0 <= r <= 255) and (0 <= g <= 255) and (0 <= b <= 255):
            return True
        else:
            print(f'Цвет R={r} G={g} B={b} не соответствует формату RGB')
            return False

    def __is_valid_sides(self, *new_sides):
        for i in range(len(new_sides)):
            if new_sides[i] <= 0:
                print('Длина сторон не может быть меньше нуля')
                return False
        if self.sides_count != len(new_sides):  # если кол-во сторон != кол-ву сторон фигуры
            return False
        return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):
        return self.__color

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = [*new_sides]

    def get_sides(self):
        return self.__sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, rgb, *sides):
        super().__init__(rgb, *sides)
        self.__radius = self.get_radius()

    def get_radius(self):
        return self.get_sides()[0] / (2 * 3.14)

    def get_square(self):
        return 3.14 * self.get_radius()**2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, rgb, *sides):
        super().__init__(rgb, *sides)

    def get_square(self):
        p = sum(self.get_sides()) / 2
        return sqrt(p*(p-self.get_sides()[0]) * (p-self.get_sides()[1]) * (p-self.get_sides()[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, rgb, *sides):
        self.__sides = []
        if len(sides) == 1:
            for i in range(self.sides_count):
                self.__sides.append(sides[0])
        super().__init__(rgb, *sides)

    def get_volume(self):
        return 6 * self.get_sides()[0]**2


print('\n===работа с окружностью===\n')
circle1 = Circle((200, 200, 100), 10, 20)  # окружность (RGB) с длиной окружности 1 т.к. стороны != 1
print('Кол-во сторон окружности:', circle1.sides_count)
print('Длина окружности:', circle1.get_sides())
print('Цвет окружности:', circle1.get_color())
print()
circle1 = Circle((100, 150, 200), 10)  # окружность (RGB), с длиной окружности 10
print('Кол-во сторон окружности:', circle1.sides_count)
print('Длина окружности:', circle1.get_sides())
print('Цвет окружности:', circle1.get_color())
print()
circle1.set_color(55, 66, 77)  # установить новый RGB окружности
print('Новый цвет окружности:', circle1.get_color())
circle1.set_color(255, 266, 277)  # попытка установить некорректный RGB окружности
print('Цвет окружности:', circle1.get_color())
print()
circle1.set_sides(20, 30)  # попытка установить неверные значения длины
print('Длина окружности:', circle1.get_sides())
circle1.set_sides(15)  # установить новое значение длины окружности
print('Новая длина окружности:', circle1.get_sides())
print()
print('Площадь круга:', circle1.get_square())

print('\n===работа с треугольником===\n')
triangle1 = Triangle((130, 140, 150), 10, 15)  # треугольник (RGB), cо сторонами = 1 (sides != 3)
print('Кол-во сторон треугольника:', triangle1.sides_count)
print('Длина треугольника:', triangle1.get_sides())
print('Цвет треугольника:', triangle1.get_color())
print()
triangle1 = Triangle((133, 144, 155), 10, 15, 20)  # треугольник (RGB), cо сторонами (10, 15, 20)
print('Кол-во сторон треугольника:', triangle1.sides_count)
print('Длина треугольника:', triangle1.get_sides())
print('Цвет треугольника:', triangle1.get_color())
print()
triangle1.set_color(57, 67, 77)  # установить новый RGB треугольника
print('Новый цвет треугольника:', triangle1.get_color())
triangle1.set_sides(13, 15, 17)  # установить новое значение длин сторон треугольника
print('Новое значение длин сторон треугольника:', triangle1.get_sides())
print()
print('Площадь треугольника:', triangle1.get_square())

print('\n===работа с кубом===\n')
cube1 = Cube((130, 140, 150), 5, 10)  # куб (RGB), cо сторонами = 1 (sides != 1 or 12)
print('Кол-во сторон куба:', cube1.sides_count)
print('Длина ребра куба:', cube1.get_sides())
print('Цвет куба:', cube1.get_color())
print()
cube1 = Cube((30, 40, 50), 5)  # куб (RGB), cо сторонами = 5
print('Кол-во сторон куба:', cube1.sides_count)
print('Длина ребра куба:', cube1.get_sides())
print('Цвет куба:', cube1.get_color())
print()
cube1.set_sides(25)  # попытка установить неверные значения длины
print('Длина ребра куба:', cube1.get_sides())
cube1.set_sides(9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, )  # установить новые значения длины
print('Новая длина ребра куба:', cube1.get_sides())
cube1.set_color(128, 138, 148)  # установить новый RGB куба
print('Новый цвет куба:', cube1.get_color())
print()
print('Площадь куба:', cube1.get_volume())
