from math import pi
#definir funciones

def  calcular_area_circulo(radio):
    return pi * (radio**2)

def calcular_perimetro_circulo(radio):
    return 2 * pi * radio

#programa principal
radio = float(input("Ingrese el valor de radio: "))

if radio < 0: 
    print("El radio no puede ser negativo.")
else: 
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"El área del círculo es: {area:.2f}")
    print(f"El períemtro del círculo es: {perimetro:.2f}")