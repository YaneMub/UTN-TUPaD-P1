# Escribe un programa que permita al usuario ingresar 100 números enteros. 
# Luego, el programa debe indicar cuántos de estos números son pares, 
# cuántos son impares, cuántos son negativos y cuántos son positivos. 

par = 0
impar = 0
negativo = 0
positivo = 0

for i in range(100):
    num = int(input("Ingrese un número entero: "))
    
    if num % 2 == 0:
        par += 1
    else:
        impar += 1

    if num >= 0:
        positivo += 1
    else:
        negativo += 1

print(f""" 
Hay {par} números pares, {impar} números impares, {positivo} números positivos, y {negativo} números negativos.
""")