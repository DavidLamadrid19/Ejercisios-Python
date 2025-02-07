# Ejercicio 1 (David Lamadrid Solar): Resolución de la fórmula general cuadrática en Python

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

discriminante = b**2 - 4*a*c

if discriminante >= 0:
    x1 = (-b + (discriminante)**0.5) / (2 * a)
    x2 = (-b - (discriminante)**0.5) / (2 * a)
    print("Las soluciones son:", x1, "y", x2)
else:
    parte_real = -b / (2 * a)
    parte_imaginaria = (abs(discriminante)**0.5) / (2 * a)
    print(f"Las soluciones son complejas: {parte_real} + {parte_imaginaria}i y {parte_real} - {parte_imaginaria}i")

