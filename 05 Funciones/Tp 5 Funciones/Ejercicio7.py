#Definir funciones

def  operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    #Cuando devuelves múltiples valores separados por comas, Python los empaqueta en una tupla automáticamente.
    return (suma, resta, multiplicacion, division) 

#Programa principal

num1 = int(input("Ingrese el número 1: "))
num2 = int(input("Ingrese el número 2: "))

resultados = operaciones_basicas(num1, num2)

print(f"\nOperaciones con {num1} y {num2}:")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")
