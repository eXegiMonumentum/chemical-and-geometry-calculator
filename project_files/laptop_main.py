
from pprint import pprint
from pola_calc import *
from concentration_calc import *


class Device(ConcentrationCalculator):
    def __init__(self, functionality, year_of_production):
        self.functionality = functionality
        self.year_of_production = year_of_production

    def message(self):
        return f"I'm the device. My year of production is {self.year_of_production}"


class Laptop(Device):
    def __init__(self, functionality, year_of_production, computing_power, weight):
        super().__init__(functionality, year_of_production)
        self.computing_power = computing_power
        self.weight = weight

    def count_figure_volume_and_area(self, geometric_figure):
        self.geometric_figure = geometric_figure

        if isinstance(geometric_figure.count, (Cuboid, Cube)):
            self.surface_area = geometric_figure.count.count_surface_area()
            self.volume = geometric_figure.count.count_volume()
            return f'Area of {geometric_figure.count.__class__.__name__}: {self.surface_area}\nVolume: {self.volume}\n'
        else:
            self.area = geometric_figure.count.count_surface_area()
            return f'Area of {geometric_figure.count.__class__.__name__}: {self.area}\n'

    def count_chemical_concentrations(self):
        main()


# Tworzenie instancji obiektu Laptop
laptop = Laptop("Mobile", 2018, 343224, 1.4)

# Tworzenie instancji obiektów dla obliczeń
rectangle = GeometricFigure(Rectangle(4, 2))
cuboid = GeometricFigure(Cuboid(Rectangle(3, 4), height=6))
square = GeometricFigure(Square(2))
cube = GeometricFigure(Cube(Square(4)))


# Obliczanie pola powierzchni lub objętości
results_list = []
results_list.append(laptop.count_figure_volume_and_area(rectangle))
results_list.append(laptop.count_figure_volume_and_area(cuboid))
results_list.append(laptop.count_figure_volume_and_area(square))
results_list.append(laptop.count_figure_volume_and_area(cube))
for i in results_list:
    print(i)

# wywołanie funkcji main z pliku concentration_calc
laptop.count_chemical_concentrations()
