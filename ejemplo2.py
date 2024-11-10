try:
    archivito = open("C:/Users/user/Documents/Codigos Python 3er Semestre/herencia.py","r")
    data = archivito.read()
except IOError:
    print("Error al leer el archivo")
finally:
    archivito.close()