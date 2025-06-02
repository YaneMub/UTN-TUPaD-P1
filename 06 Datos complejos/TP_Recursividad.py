"""EJERCICIO 1

Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario

"""

def factorial(num):
    if num == 0:
        fact = 1
    else:
        fact = factorial(num - 1) * num
    return fact

# Pedir al usuario un número entero
n = int(input("Ingresa un número entero: "))

# Mostrar el factorial de todos los números desde 1 hasta n
for i in range(1, n + 1):
    print(f"El factorial de {i} es {factorial(i)}")




"""EJERCICIO 2

Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique

"""

def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else: 
        return fibonacci(posicion - 1 )+ fibonacci(posicion - 2)
    
print(fibonacci(5))

# Pedir al usuario una posición
n = int(input("Ingrese hasta qué posición quiere ver la serie de Fibonacci: "))

# Mostrar la serie completa
print("Serie de Fibonacci:")
for i in range(n + 1):
    print(f"F({i}) = {fibonacci(i)}")




"""EJERCICIO 3

Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula 𝑛
𝑚 = 𝑛 ∗ 𝑛
(𝑚−1)
. Prueba esta función en un
algoritmo general.

"""

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
    
# Pedimos al usuario la base y el exponente
base = int(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente: "))

# Calculamos y mostramos la potencia
resultado = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es igual a {resultado}")



"""EJERCICIO 4

Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.

"""
decimal = []

def convertir_Binario(num):
    if num < 2:
        return str(num)
    else:
        return convertir_Binario(num // 2) + str(num % 2)

print(convertir_Binario(10))



"""EJERCICIO 5

Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.
 Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed().

-> PALÍNDROMO: Palabra que se lee igual al derecho y al revés.

"""

# Importamos el módulo unicodedata, que nos permite manipular y analizar caracteres Unicode.
import unicodedata

# Definimos la función que va a limpiar la palabra (sacar tildes y convertir a minúscula)
def limpiar_palabra(palabra):
    palabra = palabra.lower() 
    # Normalizamos la palabra usando 'NFD'.
    # Esto separa letras acentuadas en dos partes: la letra base + el acento.
    palabra = ''.join(
        # Este bucle recorre cada carácter "c" de la palabra normalizada.
        c for c in unicodedata.normalize('NFD', palabra)
        # Filtramos los caracteres: solo nos quedamos con los que NO sean tildes u otros adornos.
        if unicodedata.category(c) != 'Mn'
    ) #usamos join para unir todo ya transformado (en minuscula y sin tildes).
    return palabra

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])


entrada = input("Ingresa una palabra: ")
palabra_limpia = limpiar_palabra(entrada)
print(es_palindromo(palabra_limpia))



"""EJERCICIO 6

Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.

"""

def suma_digitos(n):
    if n < 10:
        return n
    else:
       #El operador % (módulo) devuelve el resto de una división, saca el último dígito de num.
       # n // 10 → Quita el último dígito
       return (n % 10) + suma_digitos(n // 10) # Es decir, retornamos el último dígito y 
       #le devolvemos a la función la división entera de num sin el resto para sumar 1 dígito a la vez.

num = int(input("Ingresa el número que deseas sumar: "))
print("La suma de sus dígitos es:", suma_digitos(num))



"""EJERCICIO 7

Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.

"""

def contar_bloques(num):
    if num == 1:
        return num 
    else:
        return num + contar_bloques(num - 1)
    
print(contar_bloques(4))



"""EJERCICIO 8

Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.

"""

def contar_digito(numero, digito):

    if numero <= 0:
        print("El número ingresado debe ser positivo.")
        return 0  # Devuelve algo para que no devuelva "none"
     
    if numero < 10:
        if numero == digito:
            return 1
        else:
            return 0
    else:
        if numero % 10 == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)
        
        
numero = int(input("Ingrese un número entero: "))
digito = int(input("Ingresa un dígito: "))

print(contar_digito(numero,digito))