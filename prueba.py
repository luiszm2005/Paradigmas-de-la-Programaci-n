class Jugador:  
    def __init__(self, nombre, numero):  
        self.__nombre = nombre  # Atributo privado  
        self.__numero = numero  # Atributo privado  

    # Método getter para nombre
    def get_nombre(self):  
        return self.__nombre

    # Método setter para nombre 
    def set_nombre(self, nuevo_nombre):  
        self.__nombre = nuevo_nombre
        
    def get_numero(self):  
        return self.__numero 

    # Método setter para numero
    def set_numero(self, nuevo_numero):  
        if self.__numero == nuevo_numero:
            print("No se puede utilizar el mismo número")
        else:
            self.__numero = nuevo_numero

# Ejemplo de uso  
jugador = Jugador("Raúl Jímenez", 9)  

# Accediendo a los atributos mediante getters  
print(jugador.get_nombre())  # Imprime: Raúl Jímenez
print(jugador.get_numero())  # Imprime: 9

# Modificando los atributos mediante setters  
jugador.set_nombre("Henry Martin")  
jugador.set_numero(9)  

# Verificando los cambios  
print(jugador.get_nombre())  # Imprime: Henry Martin  
print(jugador.get_numero())  # Imprime: 10
 