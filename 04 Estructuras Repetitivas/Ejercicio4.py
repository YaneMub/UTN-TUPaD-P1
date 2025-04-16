#Elabora un programa que permita al usuario ingresar números 
# enteros y los sume en secuencia. 
# El programa debe detenerse y mostrar el total acumulado 
# cuando el usuario ingrese un 0

numero = float("inf")
suma = 0
alto = "0"

while numero != int(alto): 
    numero = int(input("Ingrese un número entero (" + alto + " para dejar de sumar): "))
    suma += numero
    
print(f"El total acumulado es: {suma}")