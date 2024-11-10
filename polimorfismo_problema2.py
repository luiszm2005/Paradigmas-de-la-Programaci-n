from typing import List
import os
os.system("cls")

# Create the Character class
class Character:
    # Initialize name and level attributes
    def __init__(self, name, level):
        self.name = name
        self.level = level
        
    # Add attack method
    def attack(self):
        return f"{self.name} has attacked with a power of level {self.level}!"

# Create derived class Player
class Player(Character):
    def __init__(self, name, level, group):
        # Inherit attributes of Characters
        super().__init__(name, level)
        # Add the class attribute
        self.group = group
        
    # Using polymorphism by rewriting 
    # the attack message for the Player class
    def attack(self):
        return f"{self.name}, the {self.group}, attacks with a level {self.level} special attack!"
    
    # Add method useSpecialAbility()
    def useSpecialAbility(self):
        return f"{self.name} uses his special ability: Electric Lightning!"

# Create Enemy derived class
class Enemy(Character):
    def __init__(self, name, level, type):
        # Inherit Character Attributes
        super().__init__(name, level)
        # Add type attribute
        self.type = type
    
    # Using polymorphism by rewriting 
    # the attack message for the Enemy class
    def attack(self):
        return f"{self.name}, the {self.type}, launches a level {self.level} fierce attack!"
        
    # Add shout method
    def shout(self):
        return f"{self.name}, the {self.type}, shouts: Roaaaaarrr!"

# Create a character arrangement
characters = [
    Player("Aragorn", 5, "Warrior"),
    Enemy("Sauron", 10, "Dark Lord"),
    Player("Legolas", 4, "Archer")
]

# Walk through the arrangement and show the attack of each character.
print("Character attacks:")
print("-" * 50)
for character in characters:
    print(character.attack())

# Create Player and Enemy instances
player = Player("Aragorn", 5, "Warrior")
enemy = Enemy("Sauron", 10, "Dark Lord")

# Calling methods
print(player.useSpecialAbility())
print(enemy.shout())
