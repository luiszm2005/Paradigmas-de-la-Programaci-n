class CalificacionInvalida(Exception):
    pass

def insertar_calificacion(calificacion):
    if calificacion < 0:
        raise CalificacionInvalida("La calificación no puede ser negativa.")
    return f"Calificación {calificacion} insertada correctamente."

try:
    calificacion = int(input("Introduce la calificación: "))
    mensaje = insertar_calificacion(calificacion)
    print(mensaje)
except CalificacionInvalida as e:
    print(f"Error: {e}")
except ValueError:
    print("Por favor, introduce un número válido.")