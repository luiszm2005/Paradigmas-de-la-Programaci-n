from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Cuadrado(Shape):
    def __init__(self, lado): 
        self.lado = lado
        
    def area(self):
        return self.lado * self.lado

cuadrado = Cuadrado(4)
print("Área del cuadrado:", cuadrado.area())
