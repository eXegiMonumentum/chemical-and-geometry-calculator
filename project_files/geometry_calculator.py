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

class Cuboid:
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

class Cone:
    def __init__(self, base_radius, height):
        self.base_radius = base_radius
        self.height = height

    def count_base_area(self):
        return pi * self.base_radius ** 2

    def count_side_surface_area(self):
        slant_height = sqrt(self.base_radius**2 + self.height**2)
        return pi * self.base_radius * slant_height

    def count_total_surface_area(self):
        return self.count_base_area() + self.count_side_surface_area()

    def count_volume(self):
        return (pi * self.base_radius ** 2 * self.height) / 3

def geometry_calculator():
    while True:
        print("""
        Choose a shape:
        1. Rectangle (area)
        2. Cuboid (area & volume)
        3. Cone (area & volume)
        4. Back to main menu
        """)
        choice = input("Choose (1-4): ")

        try:
            if choice == "1":
                width = float(input("Enter width: "))
                height = float(input("Enter height: "))
                rectangle = Rectangle(width, height)
                print(f"Surface area: {rectangle.count_surface_area()}")

            elif choice == "2":
                width = float(input("Enter base width: "))
                height = float(input("Enter base height: "))
                depth = float(input("Enter depth: "))
                base = Rectangle(width, height)
                cuboid = Cuboid(base, depth)
                print(f"Surface area: {cuboid.count_surface_area()}, Volume: {cuboid.count_volume()}")

            elif choice == "3":
                radius = float(input("Enter base radius: "))
                height = float(input("Enter height: "))
                cone = Cone(radius, height)
                print(f"Base area: {cone.count_base_area()}, Surface area: {cone.count_total_surface_area()}, Volume: {cone.count_volume()}")

            elif choice == "4":
                break
            else:
                print("Invalid choice, please try again.")

        except ValueError:
            print("Invalid input. Please enter numerical values.")
