class Shape:
    def __init__(self, color):
        self.__color = color        # Encapsulation: private

    def get_color(self):
        return self.__color

    def area(self):                 # Polymorphism: overridden below
        pass

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.__radius = radius

    def area(self):
        return f"🔵 Circle  | Color: {self.get_color()} | Area: {3.14 * self.__radius**2:.2f}"

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.__width = width
        self.__height = height

    def area(self):
        return f"🟥 Rectangle | Color: {self.get_color()} | Area: {self.__width * self.__height}"

class Triangle(Shape):
    def __init__(self, color, base, height):
        super().__init__(color)
        self.__base = base
        self.__height = height

    def area(self):
        return f"🔺 Triangle | Color: {self.get_color()} | Area: {0.5 * self.__base * self.__height}"

# Polymorphism in action
shapes = [Circle("Blue", 7), Rectangle("Red", 5, 10), Triangle("Green", 6, 8)]

for shape in shapes:
    print(shape.area())