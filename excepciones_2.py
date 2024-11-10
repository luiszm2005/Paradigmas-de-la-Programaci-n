from typing import List
import os
os.system("cls")

# Create a custom exception for invalid character levels
class InvalidLevelException(Exception):
    def __init__(self, message):
        super().__init__(message)

# Base class Character
class Character:
    # Initialize name and level attributes
    def __init__(self, name, level):
        self.name = name
        
        # Check that the level is not less than 1
        if level < 1:
            raise InvalidLevelException(f"Invalid level for {self.name}: Level must be at least 1.")
        
        self.level = level
        
    # Attack method
    def attack(self):
        # Check if the level is at least 5 to perform an attack
        if self.level < 5:
            raise InvalidLevelException(f"{self.name} cannot attack because their level is below 5.")
        return f"{self.name} has attacked with a power of level {self.level}!"

# Derived class Player
class Player(Character):
    def __init__(self, name, level, group):
        # Inherit attributes from Character
        super().__init__(name, level)
        # Add the group attribute
        self.group = group
        
    # Overwriting the attack method for the Player class
    def attack(self):
        # Check if the level is at least 5 to perform an attack
        if self.level < 5:
            raise InvalidLevelException(f"{self.name} cannot attack because their level is below 5.")
        return f"{self.name}, the {self.group}, attacks with a level {self.level} special attack!"
    
    # Method to use the player's special ability
    def useSpecialAbility(self):
        return f"{self.name} uses his special ability: Electric Lightning!"

# Derived class Enemy
class Enemy(Character):
    def __init__(self, name, level, type):
        # Inherit attributes from Character
        super().__init__(name, level)
        # Add the type attribute
        self.type = type
    
    # Overwriting the attack method for the Enemy class
    def attack(self):
        # Check if the level is at least 5 to perform an attack
        if self.level < 5:
            raise InvalidLevelException(f"{self.name} cannot attack because their level is below 5.")
        return f"{self.name}, the {self.type}, launches a level {self.level} fierce attack!"
        
    # Method for the enemy to shout
    def shout(self):
        return f"{self.name}, the {self.type}, shouts: Roaaaaarrr!"

# Function to handle exceptions and test the code
def test_characters():
    # Function to create and test characters and handle exceptions
    try:
        # Create valid characters
        characters = [
            Player("Gimli", 6, "Dwarf"),
            Enemy("Smaug", 12, "Dragon"),
            Player("Boromir", 5, "Warrior"),  # These characters have valid levels
        ]

        # Display the attack of each character
        print("Character attacks:")
        print("-" * 50)
        for character in characters:
            print(character.attack())

    except InvalidLevelException as e:
        print(f"Error: {e}")
    
    try:
        # Create a character with an invalid level
        invalid_character = Player("Sam", 0, "Hobbit")  # This will raise an exception

    except InvalidLevelException as e:
        print(f"Error: {e}")

# Run the test function
test_characters()
