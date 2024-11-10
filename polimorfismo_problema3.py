from typing import List
import os
os.system("cls")

# Create class called palette
class Palette:
    def __init__(self, flavor: str, price: float):
        # Initialize flavor and price attributes
        self.flavor = flavor
        self.price = price
        
    # Add method showInformation()
    def showInformation(self):
        return (
            f"The flavor of the palette is: {self.flavor}\n"
            f"Its price is: ${self.price}\n"
        )
    
# Create derived class WaterPalette
class WaterPalette(Palette):
    def __init__(self, flavor: str, price: float, water_base: bool):
        # Inherits attributes from Palette class
        super().__init__(flavor, price)
        # Add additional attribute
        self.water_base = water_base
        
    # Overwrite the showInformation() method for 
    # the WaterPalette class
    def showInformation(self):
        return (
            f"The palette is made of water: {self.water_base}\n"
            f"Its price is: ${self.price}\n"
            f"Its flavor is: {self.flavor}\n"
        )
        
# Create derived class CreamPalette
class CreamPalette(Palette):
    def __init__(self, flavor: str, price: float, creamy: bool):
        # Inherits attributes from Palette class
        super().__init__(flavor, price)
        # Add additional attribute
        self.creamy = creamy
        
    # Overwrite the showInformation() method for 
    # the CreamPalette class
    def showInformation(self):
        return (
            f"The palette is made of cream: {self.creamy}\n"
            f"Its price is: ${self.price}\n"
            f"Its flavor is: {self.flavor}\n"
        )
        
# Create instances of Palette, PaletteWater and PaletteCream
palette = Palette("Grape", 10)
palette_water = WaterPalette("Lemon", 10, True)
palette_cream = CreamPalette("Vanilla", 15, True)

# Calling the methods of Palette
print(palette.showInformation())

# Calling the methods of WaterPalette
print(palette_water.showInformation())

# Calling the methods of CreamPalette
print(palette_cream.showInformation())