from typing import List
import os
os.system("cls")

from abc import ABC, abstractmethod

# Clase abstracta Vehiculo
class Vehiculo(ABC):
    def __init__(self, numero_ruedas, marca, modelo):
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo

    @abstractmethod
    def arrancar(self):
        pass

# Subclase Automovil
class Automovil(Vehiculo):
    def __init__(self, numero_ruedas, marca, modelo):
        super().__init__(numero_ruedas, marca, modelo)

    def arrancar(self):
        print(f"El automóvil {self.marca} {self.modelo} está arrancando.")

# Subclase Motocicleta
class Motocicleta(Vehiculo):
    def __init__(self, numero_ruedas, marca, modelo):
        super().__init__(numero_ruedas, marca, modelo)

    def arrancar(self):
        print(f"La motocicleta {self.marca} {self.modelo} está arrancando.")

automovil = Automovil(4, "Toyota", "Corolla")
motocicleta = Motocicleta(2, "Yamaha", "R1")

automovil.arrancar() 
motocicleta.arrancar()