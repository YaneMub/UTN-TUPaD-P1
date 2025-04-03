#Ejercicio 1

#Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Por favor, ingrese su edad: "))

if edad > 18:
    print("Es mayor de edad")
else:
    print("Usted es menor de edad")


############################################################################################

#Ejercicio 2

#Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”

nota = int(input("Por favor, ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

###########################################################################################

#Ejercicio 3

#Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". 

numero = int(input("Por favor, ingresa un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par.")
else: 
    print("Por favor, ingrese un número par.")

###########################################################################################

#Ejercicio 4

#Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad = int(input("Por favor, ingrese su edad: "))

if edad < 12:
    print("Usted es un Niño/a")
elif edad >= 12 and edad < 18:
    print("Usted es Adolescente")
elif edad >= 18 and edad < 30:
    print("Usted es un Adulto/a joven")
else:
    print("Usted es un Adulto/a")
    
###########################################################################################

#Ejercicio 5

contraseña = input("Ingrese una contraseña: ")

cantidad_caracter = len(contraseña)

if cantidad_caracter >= 8 and cantidad_caracter <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

###########################################################################################

#Ejercicio 6

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

if media > mediana and mediana > moda:
    print("Sesgo positivo")
elif media < mediana and mediana < moda:
    print ("Sesgo negativo")
elif media == mediana == moda:
    print("Sin Sesgo")
else:
    print("Todos los valores son diferentes")

###########################################################################################

#Ejercicio 7

#Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.

#strip() quita los espacios
palabra = input("Ingrese una palabra: ").strip()

#-1 toma el último elemento de palabra y lower() convierte la letra en minúscula.
ultima_letra = palabra[-1].lower()

if ultima_letra in ("a", "e", "i", "o", "u"):
    palabra += "!"

print(palabra)

###########################################################################################

#Ejercicio 8

nombre = input("Ingrese su nombre:")
formato = int(input( 
    "Si quiere su nombre en mayúscula ingrese 1.\n" 
    "Si quiere su nombre en minúscula ingrese 2.\n" 
    "Si quiere la primer letra de su nombre en mayúscula ingrese 3.\n"
))

if formato == 1:
    print(nombre.upper())
elif formato == 2:
    print(nombre.lower())
elif formato == 3:
    print(nombre.title())

###########################################################################################

#Ejercicio 9

magnitud = float(input("Por favor, ingrese la magnitud del terremoto:"))

if magnitud < 3:
    print("Muy leve")
elif magnitud < 4:
    print("Leve")
elif magnitud < 5:
    print("Moderado")
elif magnitud < 6:
    print("Fuerte")
elif magnitud < 7:
    print("Muy Fuerte")
else:
    print("Extremo")

###########################################################################################

#Ejercicio 10

hemisferio = input("¿En cuál hemisferio te encuentras? (N o S)")
mes = int(input("Ingresa el número del mes actual: "))
dia = int(input("Ingresa el día actual:"))

if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"

if (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"

if (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"

if (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"

if hemisferio == "N":
    print(estacion_norte)
if hemisferio == "S":
    print(estacion_sur)