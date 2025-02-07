# Ejercicio 9(David Lamadrid Solar) Calcular el ángulo α del triángulo
import math

a = float(input("Ingrese el valor del lado a: "))
b = float(input("Ingrese el valor del lado b: "))
c = float(input("Ingrese el valor del lado c: "))

s = (a + b + c) / 2

alpha_rad = math.asin((2 * s) / (b * c))
alpha_deg = (180 / math.pi) * alpha_rad

print(f"El ángulo α es aproximadamente {alpha_deg:.2f} grados.")
