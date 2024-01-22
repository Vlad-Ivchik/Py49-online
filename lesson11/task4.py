from math import pi


class Sphere:
    def __init__(self, *arg):
        if len(arg) == 0:
            arg = (1, 0, 0, 0)
        elif len(arg) == 1:
            arg = (arg[0], 0, 0, 0)
        self.radius, self.x, self.y, self.z = arg

    def get_volume(self):
        return (4 / 3) * pi * (self.radius ** 3)

    def get_square(self):
        return 4 * pi * (self.radius ** 2)

    def get_radius(self):
        return self.radius

    def get_center(self):
        return self.x, self.y, self.z

    def set_radius(self, radius):
        self.radius = radius

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        return (self.x ** 2) - x + (self.y ** 2) - y + (self.z ** 2) - z < self.radius ** 2


result = Sphere()
print("Объем шара, ограниченного текущей сферой:", result.get_volume())
print("Площадь внешней поверхности сферы:", result.get_square())
print("Радиус текущей сферы:", result.get_radius())
print("Кортеж с координатами центра сферы:", result.get_center())
result.set_radius(2)
print("Поменяем радиус сферы на", result.get_radius())
result.set_center(1, 1, 1)
print("Поменяем центр сферы на", result.get_center())
print("Точка (4,2,1) внутри сферы?", result.is_point_inside(4, 2, 1))


#task4