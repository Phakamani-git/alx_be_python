import math

class Shape:
    """Base class for geometric shapes."""
    def area(self):
        raise NotImplementedError("Subclasses must override the area() method")


class Rectangle(Shape):
    """Represents a rectangle shape."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    """Represents a circle shape."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
