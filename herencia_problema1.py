# Call the math library to be able to 
# to make operations for the area of the circle
import math

# Create class called GeometricFigure
class GeometricFigure:
    # Create name attribute
    def __init__(self, name) -> None:
        self.name = name
     
    # Create method calculateArea()   
    def calculateArea(self):
        pass
   
# Derived class Circle 
class Circle(GeometricFigure):
    def __init__(self, radius):
        # Inherit the class GeometricFigure
        # Initialize the radius attribute to be able to take the radius and calculate the area
        super().__init__("Circle")
        self.radius = radius
    
    # Calculate area of circle
    def calculateArea(self):
        return math.pi * self.radius ** 2
    
# Derived class Rectangle
class Rectangle(GeometricFigure):
    def __init__(self, width, high):
        # Inherit the class GeometricFigure
        # Initialize the width and height attribute to be able to extract the area
        super().__init__("Rectangle")
        self.width = width
        self.high = high
    
    # Calculate the area of the rectangle
    def calculateArea(self):
        return self.width * self.high

# Triangle derivative class
class Triangle(GeometricFigure):
    def __init__(self, base, height):
        # Inherit the class GeometricFigure
        # Initialize the base and height attribute to be able to get the area
        super().__init__("Triangle")
        self.base = base
        self.height = height
    
    # Calculate area of triangle
    def calculateArea(self):
        return (self.base * self.height) / 2

# Examples of use
circle = Circle(10)
print(f"Area of the {circle.name}: {circle.calculateArea():.2f}")
# Area of the Circle: 78.54

rectangle = Rectangle(5, 7)
print(f"Area of the {rectangle.name}: {rectangle.calculateArea()}")
# Area of the Rectangle: 24

triangle = Triangle(4, 9)
print(f"Area of the {triangle.name}: {triangle.calculateArea()}")
# Area of the Triangle: 12