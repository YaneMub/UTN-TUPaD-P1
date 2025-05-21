#Definir funciones
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

#Programa principal
celsius = float(input("Ingresa los grados Celsius: "))

conversorF = celsius_a_fahrenheit(celsius)
print(f"El equivalente de {celsius}°C a Fahrenheit, es {conversorF}°F")
