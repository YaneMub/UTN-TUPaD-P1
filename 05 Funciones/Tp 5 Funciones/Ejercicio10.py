#Definir funciones
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

#Programa principal
num1 = float(input("Ingrese el primer valor: "))
num2 = float(input("Ingrese el segundo valor: "))
num3 = float(input("Ingrese el tercer valor: "))

promedio = calcular_promedio(num1, num2, num3)
print(f"El promedio final es de {promedio:.2f}")