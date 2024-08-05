
from math import sqrt, pi


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def count_surface_area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)


# class Cube():
#     def __init__(self, square: Square):
#         self.square = square

#     def count_surface_area(self):
#         return self.square.count_surface_area() * 6

#     def count_volume(self):
#         return self.square.count_surface_area() * self.square.height


class Cuboid():
    def __init__(self, base_figure, height):
        self.base = base_figure
        self.height = height

    def count_volume(self):
        return self.base.count_surface_area() * self.height

    def count_surface_area(self):
        return 2 * self.base.count_surface_area() + 2 * self.base.width * self.height + 2 * self.base.height * self.height


class Cube(Cuboid):
    def __init__(self, base_figure: Square):
        super().__init__(base_figure, base_figure.height)


class GeometricFigure:
    def __init__(self, figure):
        self.count = figure

    def count_surface_area(self):
        return self.count.count_surface_area()


# class RightTriangle:
#     def __init__(self, baseSide, height):
#         self.baseSide = baseSide
#         self.height = height

#     def count_triangle_area(self):
#         return 1/2 * (self.baseSide * self.height)

#     def count_counter_rectangle(self):
#         counterRectangle = sqrt((self.baseSide) ** 2 + (self.height ** 2))
#         return counterRectangle  # l side in Cone

# # przekrój osiowy dziedzczy z trójkąta prostokątnego.


# class Cone(RightTriangle):
#     def __init__(self, baseSide, height):
#         super().__init__(baseSide, height)

#     def count_cone_base_area(self):
#         return pi * self.baseSide ** 2

#     def count_cone_side_surface(self):
#         return pi * self.baseSide * self.count_counter_rectangle()

#     def count_cone_surface(self):
#         return ((pi * self.baseSide ** 2) + pi * self.baseSide * self.count_counter_rectangle())

#     def count_cone_volume(self):
#         return (pi * (self.baseSide ** 2) * self.height) / 3


# cone = Cone(3, 5)
# print(cone.count_cone_base_area())
# print(cone.count_cone_side_surface())
# print(cone.count_cone_surface())
# print(cone.count_cone_volume())
