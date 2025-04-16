#Desarrolla un programa que solicite al usuario un número 
#entero y determine la cantidad de dígitos que contiene.

numero = int(input("Ingresa un número entero: "))
cant_digitos = len(str(numero))

print(f"El número ingresado tiene {cant_digitos} dígitos")