# Create class called palette
class Palette:
    def __init__(self, flavor: str, price: float):
        # Initialize flavor and price attributes
        self.flavor = flavor
        self.price = price
        
    # Add method showInformation()
    def showInformation(self):
        return f"The flavor of the palette is: {self.flavor} and its price is: ${self.price}." 
    
    # New functionality: Apply discount
    def applyDiscount(self, percentage):
        discount = self.price * (percentage / 100)
        self.price -= discount
        print(f"A {percentage}% discount has been applied. The new price is: ${self.price}.")
        
    # New functionality: Change flavor
    def changeFlavor(self, new_flavor):
        self.flavor = new_flavor
        print(f"The flavor of the palette has been changed to: {self.flavor}.")
        
# Create derived class WaterPalette
class WaterPalette(Palette):
    def __init__(self, flavor: str, price: float, water_base: bool):
        # Inherits attributes from Palette class
        super().__init__(flavor, price)
        # Add additional attribute
        self.water_base = water_base
        
    # Add showWaterBase() method to show if 
    # the palette has a water base or not.
    def showWaterBase(self):
        return f"It is water-based: {self.water_base}"
    
    # Add functionality to change the price in $2 
    def adjustPrice(self):
        self.price += 2
        print(f"The new price of the {self.flavor} palette is: ${self.price}.")
        
# Create derived class CreamPalette
class CreamPalette(Palette):
    def __init__(self, flavor: str, price: float, creamy: bool):
        # Inherits attributes from Palette class
        super().__init__(flavor, price)
        # Add additional attribute
        self.creamy = creamy
        
    # Add method showCreamyTexture() to show 
    # if the palette has creamy texture or not.
    def showCreamyTexture(self):
        return f"It has a creamy texture: {self.creamy}"
    
    # Add functionality to change the price by $6
    def adjustPrice(self):
        self.price += 6
        print(f"The new price of the {self.flavor} palette is: {self.price}.")
        
# Create instances of WaterPalette and CreamPalette
palette_water = WaterPalette("Lemon", 10, True)
palette_cream = CreamPalette("Vanilla", 15, True)

# Calling the methods of CreamPalette
print(palette_water.showInformation())
print(palette_water.showWaterBase())
palette_water.adjustPrice()

# Calling the methods of CreamPalette
print(palette_cream.showInformation())
print(palette_cream.showCreamyTexture())
palette_cream.adjustPrice()

# Create instances with additional functionalities
palette_water_new = WaterPalette("Strawberry", 12, True)
print(palette_water_new.showInformation())
palette_water_new.applyDiscount(10)
palette_water_new.changeFlavor("Tamarindo")
print(palette_water_new.showInformation())