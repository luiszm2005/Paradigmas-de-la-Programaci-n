# Clase base (superclase) 

class JugadorFutbol: 

    def __init__(self, nombre, posicion): 
        self.nombre = nombre 
        self.posicion = posicion 

    def realizar_accion(self): 
        return "Acción genérica de fútbol" 

# Subclase que hereda de JugadorFutbol 

class Delantero(JugadorFutbol): 

    def realizar_accion(self): 
        return "Anotar un gol" 

# Otra subclase que hereda de JugadorFutbol 

class Mediocampista(JugadorFutbol): 

    def realizar_accion(self): 
        return "Pase al compañero" 

# Subclase adicional 

class Defensa(JugadorFutbol): 

    def realizar_accion(self): 
        return "Bloquear el tiro" 

# Función que demuestra polimorfismo 

def imprimir_accion(jugador): 
    print(jugador.realizar_accion()) 

# Ejemplo de uso 

delantero = Delantero("Luis", "Delantero") 
mediocampista = Mediocampista("Andrés", "Mediocampista") 
defensa = Defensa("Carlos", "Defensa") 

imprimir_accion(delantero)      # Imprime: Anotar un gol 
imprimir_accion(mediocampista)  # Imprime: Pase al compañero 
imprimir_accion(defensa)        # Imprime: Bloquear el tiro 