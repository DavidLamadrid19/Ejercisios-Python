# Ejercicio 3 (David Lamadrid) Verificamos múltiplos

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 % num2 == 0:
    print(f"{num1} es múltiplo de {num2}")
elif num2 % num1 == 0:
    print(f"{num2} es múltiplo de {num1}")
else:
    print("Ningún número es múltiplo del otro numero")