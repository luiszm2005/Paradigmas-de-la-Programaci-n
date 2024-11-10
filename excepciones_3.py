from typing import List
import os
os.system("cls")

# Create a custom exception for invalid palette data
class InvalidPaletteException(Exception):
    pass

# Base class Palette
class Palette:
    def __init__(self, flavor: str, price: float):
        # Validate that price is greater than 0
        if price <= 0:
            raise InvalidPaletteException("Price must be greater than 0.")
        
        # Initialize flavor and price attributes
        self.flavor = flavor
        self.price = price
        
    # Method to show information
    def showInformation(self):
        return f"Flavor: {self.flavor}, Price: ${self.price}"

# Derived class WaterPalette
class WaterPalette(Palette):
    def __init__(self, flavor: str, price: float, water_base: bool):
        # Validate that water_base is True or False
        if water_base not in [True, False]:
            raise InvalidPaletteException("water_base must be True or False.")
        
        super().__init__(flavor, price)
        self.water_base = water_base
        
    # Overwriting the showInformation method
    def showInformation(self):
        return f"Water-based: {self.water_base}, {super().showInformation()}"

# Derived class CreamPalette
class CreamPalette(Palette):
    def __init__(self, flavor: str, price: float, creamy: bool):
        # Validate that creamy is True or False
        if creamy not in [True, False]:
            raise InvalidPaletteException("creamy must be True or False.")
        
        super().__init__(flavor, price)
        self.creamy = creamy
        
    # Overwriting the showInformation method
    def showInformation(self):
        return f"Creamy: {self.creamy}, {super().showInformation()}"

# Function to test palettes
def test_palettes():
    try:
        # Creating valid palettes
        palette1 = Palette("Grape", 10)
        palette2 = WaterPalette("Lemon", 8, True)
        palette3 = CreamPalette("Vanilla", 12, False)

        # Displaying palette information
        print(palette1.showInformation())
        print(palette2.showInformation())
        print(palette3.showInformation())

        # Attempt to create an invalid palette
        invalid_palette = Palette("Strawberry", -1)  # This will raise an exception
    except InvalidPaletteException as e:
        print(f"Error: {e}")
        
    try:
        
        # Attempt to create a WaterPalette with a non-boolean water_base
        invalid_water_palette = WaterPalette("Mango", 10, "Yes")  # This will raise an exception

    except InvalidPaletteException as e:
        print(f"Error: {e}")

# Run the test function
test_palettes()