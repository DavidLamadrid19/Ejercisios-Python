# Ejercicio 4 (David Lamadrid) Leer número complejo
real = float(input("Ingrese la parte real: "))
imaginaria = float(input("Ingrese la parte imaginaria: "))

# Mostramos los componentes
print("Parte real:", real)
print("Parte imaginaria:", imaginaria)

# Mostramos el número completo con j
if imaginaria >= 0:
    print(f"Número complejo: {real} + {imaginaria}j")
else:
    print(f"Número complejo: {real} - {abs(imaginaria)}j")