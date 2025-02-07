# Ejercicio n7 (David Lamadrid) Ajuste de ingredientes para galletas x
cantidad_galletas = int(input("¿Cuántas galletas desea preparar?: "))

factor = cantidad_galletas / 12
azucar = 1.5 * factor
mantequilla = 1 * factor
harina = 2.75 * factor

print(f"Necesitarás {azucar:.2f} tazas de azúcar, {mantequilla:.2f} tazas de mantequilla y {harina:.2f} tazas de harina.")
