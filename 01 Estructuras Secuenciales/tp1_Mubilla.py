# #Ejercicio 1
# print("Hola Mundo!")

# #Ejercicio 2
# nombre = input("¿Cuál es su nombre?")
# saludo = print(f"Hola {nombre}!")

# #Ejercicio 3
# nombre = input("Ingrese su nombre: ")
# apellido = input("Ingrese su apellido: ")
# edad = input("Ingrese su edad")
# lugar_residencia = input("¿Dónde vive?")

# print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}")

#Ejercicio 4
# radio = float(input("Ingrese el radio del círculo: "))
# area = 3.1416 * radio ** 2
# perimetro = 2 * 3.1416 * radio
# print(f"El area del círculo es de: {area}, y su perímetro es de: {perimetro}.")


#Ejercicio 5
# segundos = int(input("Ingrese los segundos que quiere convertir a horas: "))
# horas = segundos / 3600
# print(horas)

#Ejercicio 6
# numero = int(input("Ingrese un número entero: "))

# print(f"""
# {numero} x 0 = {numero * 0}
# {numero} x 0 = {numero * 1}
# {numero} x 0 = {numero * 2}
# {numero} x 0 = {numero * 3}
# {numero} x 0 = {numero * 4}
# {numero} x 0 = {numero * 5}
# {numero} x 0 = {numero * 6}
# {numero} x 0 = {numero * 7}
# {numero} x 0 = {numero * 8}
# {numero} x 0 = {numero * 9}
# {numero} x 0 = {numero * 10}
# """)


# #Ejercicio 7
# num1 = int(input("Ingrese un número entero que no sea 0: "))
# num2 = int(input("Ingrese otro número entero que no sea 0: "))

# suma = num1 + num2
# resta = num1 - num2
# multiplicacion = num1 * num2
# divison = num1 / num2

# print(f"""
# {num1} + {num2} = {suma}
# {num1} - {num2} = {resta}
# {num1} x {num2} = {multiplicacion}
# {num1} / {num2} = {divison}
#       """)

#Ejercicio 8
# altura = float(input("Ingrese su altura en metros: "))
# peso = float(input("Ingrese su peso en kg: "))

# IMC = peso / (altura ** 2)

# print(f"Su Índice de masa corporal es de: {IMC}")

#Ejercicio 9
# celsius = float(input("Ingrese una temperatura en °C: "))
# fahrenheit = 9/5 * celsius + 32

# print(f"Los °C ingresados equivalen a {fahrenheit} °F")

#Ejercicio 10
num1 = int(input("Ingrese un número (entero): "))
num2 = int(input("Ingrese otro número (entero): "))
num3 = int(input("Ingrese el último número (entero): "))

promedio = (num1 + num2 + num3) / 3

print("El promedio final es de: ", promedio)