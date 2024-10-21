from math import pi, sqrt

class Figure:
    sides_count = 0

    def __init__(self, color, *sides, filled = True):
        if self.__is_valid_color(color):
            self.__color = list(color)
        if self.__is_valid_sides(sides):
            self.__sides = list(sides)
        elif not self.__is_valid_sides(sides) and len(sides) != 1:
            self.__sides = []
            for i in range(0, self.sides_count):
                self.__sides.append(1)
        elif not self.__is_valid_sides(sides) and len(sides) == 1:
            self.__sides = []
            for i in range(0, self.sides_count):
                self.__sides.append(sides[0])

    def get_color(self):
        return self.__color

    def __is_valid_color(self, color):
        bool_ = True
        if len(color) == 3:
            for item in color:
                if item >=0 and item <= 255:
                    continue
                else:
                    bool_ = False
                    break
        else:
            bool_ = False
        return bool_

    def set_color(self, *color):
        if self.__is_valid_color(color):
            self.__color = list(color)

    def __is_valid_sides(self, sides):
        bool_ = False
        if len(sides) == self.sides_count:
            bool_ = True
        return bool_

    def get_sides(self):
        return self.__sides

    def __len__(self):
        res = 0
        for item in self.__sides:
            res += item
        return res

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1
    circle_bool = True

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = sides[0] / (2 * pi)

    def get_square(self):
        self.__radius = self.get_sides()[0] / (2 * pi)
        return pi *( self.__radius ** 2)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        perimeter = sum(self.get_sides(), 0)
        half_meter = perimeter / 2
        return sqrt(half_meter * (half_meter - self.get_sides()[0]) *
                    (half_meter - self.get_sides()[1]) * (half_meter - self.get_sides()[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color,*sides)
    def get_volume(self):
        return self.get_sides()[0] ** 3

if __name__ == '__main__':
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

