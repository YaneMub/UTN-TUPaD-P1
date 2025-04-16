# Elabora un programa que permita al usuario ingresar 100 números enteros 
# y luego calcule la media de esos valores.


suma = 0

for i in range(100):
    num = int(input("Ingrese un número entero: "))
    suma += num

print(f"El promedio de los valores ingresados es de: ", suma/10)