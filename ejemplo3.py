try:
    x = int(input("Introduce un numero: "))

except ValueError:
    print("Debes introducir un numero valido.")
else:
    print(f"El numero es {x}")