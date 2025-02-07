# Ejercicio 6(David Lamadrid) Calcular la cuenta en un restaurante random
valor_platoo = float(input("Ingrese el valor del plato: "))
impu_consumo = valor_platoo * 0.08
propinaa = valor_platoo * 0.10
total = valor_platoo + impu_consumo + propinaa

print("Impuesto al consumo (8%):", impu_consumo)
print("Propina (10%):", propinaa)
print("Total a pagar:", total)