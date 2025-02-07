# Ejercicio 8(David joel Lamadri solar) Cálculo de kilómetros recorridos de un carro
galones = float(input("Ingrese la cantidad de galones de gasolina: "))
mpg = 9.2
millas = galones * mpg
kilometros = millas * 1.60934

print(f"Con {galones} galones, puede recorrer aproximadamente {kilometros:.2f} kilómetros.")