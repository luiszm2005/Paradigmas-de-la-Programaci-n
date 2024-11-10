class Jugador:
    def __init__(self, nombre, nacionalidad) -> None:
        self.nombre = nombre 
        self.nacionalidad = nacionalidad
        
    def numero(self):
            return 10
            
    def info(self):
            return f"Soy {self.nombre} y mi nacionalidad es {self.nacionalidad}"
        
class America(Jugador):
    def __init__(self, nombre, nacionalidad, goles) -> None:
        super().__init__(nombre, nacionalidad)
        self.goles = goles
         
    def numero(self):
        return 7
         
    def meter_goles(self):
        self.goles += 1
        return f"El jugador ha anotado un gol. Ahora tiene {self.goles} goles"

class Chivas(Jugador):
    def __init__(self, nombre, nacionalidad, posicion) -> None:
        super().__init__(nombre, nacionalidad)
        self.posicion = posicion
        
    def numero(self):
        return 8
        
    def info(self):
        return f"Soy el jugador {self.nombre}, soy de nacionalidad {self.nacionalidad} y mi posición es {self.posicion}"

jugador_america = America("H. Martin", "Mexicana", 8) 
jugador_chivas = Chivas("Chicharito", "Mexicana", "Delantero") 

print(jugador_america.info())
print(jugador_america.numero())  
print(jugador_america.meter_goles())

print(jugador_chivas.info())
print(jugador_chivas.numero())