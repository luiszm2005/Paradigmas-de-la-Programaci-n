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
        
    # Add shout method
    def shout(self):
        return f"{self.name}, the {self.type}, shouts: Ooooh no brother!"

# Create Player and Enemy instances
player = Player("Aragorn", 5, "Warrior")
enemy = Enemy("Sauron", 10, "Dark Lord")

# Calling methods
print(player.attack())
# Aragorn has attacked with a power of level 5!

print(player.useSpecialAbility())
# Aragorn uses his special ability: Electric Lightning!   

print(enemy.attack())
# Sauron has attacked with a power of level 10!

print(enemy.shout())
# Sauron, the Dark Lord, shouts: Ooooh no brother!  