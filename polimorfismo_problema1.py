from typing import List
import os
os.system("cls")

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
    
    # Create method description area, to show it later in a for
    def descripcionArea(self):
        return f"{self.name:<15}: Area = {self.calculateArea()}"
    
# Derived class Circle 
class Circle(GeometricFigure):
    def __init__(self, radius):
        # Inherit the class GeometricFigure
        # Initialize the radius attribute to be able to take the radius and calculate the area
        super().__init__("Circle")
        self.radius = radius
    
    # Calculate area of circle
    def calculateArea(self):
        return f"{math.pi * self.radius ** 2:.2f}"
    
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

# Create an arrangement of objects of different geometric shapes
figures = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 8)
]

# Scroll through the array and display the description of the areas.
print("Table of areas of geometric figures:")
print("-" * 50)
for figure in figures:
    print(figure.descripcionArea())
