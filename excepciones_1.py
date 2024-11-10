from typing import List
import os
os.system("cls")

# Importing the math module to perform mathematical operations
import math

# Customized exception for invalid geometric shapes
class InvalidFigureException(Exception):
    # Exception for handling invalid geometry errors in shapes
    pass

# Base class GeometricFigure
class GeometricFigure:
    # Base class representing a geometric figure
    
    # Constructor initializing the figure name
    def __init__(self, name) -> None:
        self.name = name
     
    # Method for calculating the area, which will be overwritten in derived classes
    def calculateArea(self):
        pass
    
    # Method for calculating the perimeter, which will be overwritten in derived classes
    def calculatePerimeter(self):
        pass
    
    # Method to describe the area of the figure
    def descripcionArea(self):
        return f"{self.name:<15}: Area = {self.calculateArea()}"
    
    # Method to describe the perimeter of the figure
    def descripcionPerimeter(self):
        return f"{self.name:<15}: Perimeter = {self.calculatePerimeter()}"

# Derivative class Circle
class Circle(GeometricFigure):
    # Class representing a circle
    
    # Constructor that initializes the radius and inherits from GeometricFigure
    def __init__(self, radius):
        super().__init__("Circle")  # Calls the constructor of the base class
        self.radius = radius        # Initializes the radius
    
    # Overwrites the method for calculating the area of the circle
    def calculateArea(self):
        return f"{math.pi * self.radius ** 2:.2f}"  # Area formula: πr²
    
    # Overwrites the method for calculating the perimeter of the circle
    def calculatePerimeter(self):
        return f"{2 * math.pi * self.radius:.2f}"  # Perimeter formula: 2πr

# Derived class Rectangle
class Rectangle(GeometricFigure):
    # Class representing a rectangle
    
    # Constructor that initializes width and height, and inherits from GeometricFigure
    def __init__(self, width, height):
        super().__init__("Rectangle")  # Calls the constructor of the base class
        self.width = width             # Initializes the width
        self.height = height           # Initializes the height
    
    # Overwrites the method for calculating the area of the rectangle
    def calculateArea(self):
        return self.width * self.height  # Fórmula del área: ancho * alto
    
    # Overwrites the method for calculating the perimeter of the rectangle
    def calculatePerimeter(self):
        return 2 * (self.width + self.height)  # Perimeter formula: 2(width + height)

# Derivative class Triangle
class Triangle(GeometricFigure):
    # Class representing a triangle
    
    # Constructor initializing base, height and sides of the triangle
    def __init__(self, base, height, side1, side2, side3):
        super().__init__("Triangle")  # Calls the constructor of the base class
        self.base = base              # Initializes the base
        self.height = height          # Initializes the height
        
        # Validate that the sides can form a triangle
        if not (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
            raise InvalidFigureException("Invalid triangle: the sum of any two sides must be greater than the third side.")
        
        self.side1 = side1  # Initialize side 1
        self.side2 = side2  # Initialize side 2
        self.side3 = side3  # Initialize side 3
    
    # Overwrites the method for calculating the area of the triangle
    def calculateArea(self):
        return (self.base * self.height) / 2  # Area formula: (base * height) / 2
    
    # Overwrites the method for calculating the perimeter of the triangle
    def calculatePerimeter(self):
        return self.side1 + self.side2 + self.side3  # Sum of the three sides

# Handling exceptions for perimeter and area
def create_and_show_figures():
    # Function for creating and displaying areas and perimeters of different geometric figures
    figures = []  # Ready to store geometric shapes
    try:
        # Create several valid geometric shapes
        figures.append(Circle(10))             # Circle with radius 10
        figures.append(Rectangle(3, 9))       # Rectangle with width 3 and height 9
        figures.append(Triangle(1, 1, 1, 1, 5)) # Invalid triangle of sides 1, 1 and 5
        
        # Show the areas and perimeters of the figures created.
        for figure in figures:
            print(figure.descripcionArea())       # Shows the area of the figure
            print(figure.descripcionPerimeter())  # Shows the perimeter of the figure
    
    # Capture of the custom exception InvalidFigureException
    except InvalidFigureException as e:
        print(f"Error: {e}")  # Displays the error if the triangle is invalid
    
    # ZeroDivisionError screenshot (should it occur in future cases)
    except ZeroDivisionError as e:
        print(f"Math error: {e}")  # Displays the error if division by zero occurs
    
    # Capture of any other unexpected errors
    except Exception as e:
        print(f"Unexpected error: {e}")

# Execute the function
create_and_show_figures()