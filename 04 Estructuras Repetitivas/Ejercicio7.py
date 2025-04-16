# Crea un programa que calcule la suma de todos los números comprendidos 
# entre 0 y un número entero positivo indicado por el usuario.

num = int(input("Ingresa un número positivo: "))
suma = 0 

if num > 0:

    for i in range(0,num):
        suma += i
    print(f"La suma de los números comprendidos entre 0 y {num} es {suma}")
else:
    print("Debía ser un número positivo.")