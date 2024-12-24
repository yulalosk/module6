import math
class Figure:
    sides_count = 0
    def __init__(self, color: tuple[int,int,int], *sides, filled=False):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r,g,b):
        values = 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255
        values_type = isinstance(r, int) and isinstance(g, int) and isinstance(b, int)
        return values, values_type

    def set_color(self, r, g, b):
        if self.__is_valid_color(r,g,b):
            self.__color = r, g, b

    @staticmethod
    def is_valid_sides(*sides):
        for side in sides:
            if not isinstance(side, int) or side < 0:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self,*sides):
        if len(sides) == len(self.__sides):
            valid_sides = []
            for side in sides:
                if self.is_valid_sides(side):
                    valid_sides.append(side)
            self.__sides = valid_sides



class Triangle(Figure):
    sides_count = 3
    def __init__(self, color: tuple[int, int, int], height, *sides, filled = False):
        super().__init__(color, *sides, filled=filled)
        self.height = height
    def get_square(self):
        p = (len(self) / 2)
        sides = self.get_sides()
        return math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))


class Circle(Figure):
    sides_count = 1
    def __init__(self, color: tuple[int,int,int], lengh, filled=False):
        super().__init__(color, lengh, filled=filled)
        self.__radius = lengh / (2 * math.pi)

    def get_square(self):
        return len(self) ** 2 / (4 * math.pi)



class Cube(Figure):
    sides_count = 12
    def __init__(self, color: tuple[int, int, int], side, filled=False):
        cube_sides = [side] * 12
        super().__init__(color, *cube_sides, filled=filled)

    def get_volume(self):
        return self.get_sides()[0] ** 3

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


