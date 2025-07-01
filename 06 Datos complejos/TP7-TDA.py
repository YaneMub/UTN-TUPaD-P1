"""EJERCICIO 1
  
  1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300

"""

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

# Añadir nuevos key-value
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

#print(precios_frutas)

"""EJERCICIO 2"""

# Actualización de valores
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800


print(precios_frutas)

"""EJERCICIO 3"""

# Convertir precios_frutas en una lista de elementos sin los precios.
frutas = list(precios_frutas.keys())
print(frutas)



"""EJERCICIO 4

4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe

"""
# Creamos un diccionario vacío
agenda = {}

# cargar 5 contactos mediante un bucle
for i in range(5):
    nombre = input(f"Ingresa el nombre del contacto {i + 1} ")
    numero = input(f"Ingresá el número telefónico de {nombre}: ")
    agenda[nombre] = numero

buscar = input("\n¿De qué contacto querés saber el número?: ")

if buscar in agenda: 
    print(f"El número de {buscar} es: {agenda[buscar]}")
else:
    print("Ese contacto no está en la agenda.")



"""EJERCICIO 5 

5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra.

"""

frase = input("Ingresá una frase: ")

# Convertimos la frase en una lista de palabras
palabras = frase.lower().split()
# Seleccionamos las palabras únicas
palabras_unicas = set(palabras)

print(f"Las palabras únicas son: {palabras_unicas}")

# Creamos un diccionario con la cantidad de veces que aparece cada palabra
conteo_palabras = {}

for palabra in palabras:
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1

print("Cantidad de veces que aparece cada palabra:")
print(conteo_palabras)



"""EJERCICIO 6

6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno.
Ejemplo:

"""
alumnos = {}

# Ingresar datos de 3 alumnos
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i + 1}: ")
    print("Ingresá las 3 notas (separadas por espacios): ") 
    # splir: divide la cadena con espacios.
    # map(float, ) convierte todos los elementos ingresados en decimal (map es para convertirlos en 1 misma línea, todos juntos).
    # tuple permite convertir el dato de entrada en una tupla. 
    notas = tuple(map(float, input().split()))
    
    if len(notas) != 3: #Verificamos que se hayan ingresado 3 notas. 
        print("Debés ingresar exactamente 3 notas.")
        break
    alumnos[nombre] = notas

# Mostrar promedio de cada alumno
print("Promedios:")
for nombre, notas in alumnos.items(): # .items() devuelve pares clave-valor del diccionario.
    # sum() suma todas las notas 
    # dividimos la suma por la cantidad de notas ingresadas (3)
    promedio = sum(notas) / len(notas) 
    print(f"{nombre}: {promedio:.2f}") # .2f permite indicar cuántos decimales se van a mostrar.


"""EJERCICIO 7

7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)

"""
# Estudiantes que aprobaron cada parcial
parcial_1 = {"Ana", "Luis", "Juan", "Sol", "Pedro"}
parcial_2 = {"Sol", "Pedro", "Laura", "Lucas", "Luis"}

# 1. Aprobó ambos parciales (intersección)
ambos = parcial_1 & parcial_2
print("Aprobaron ambos parciales:", ambos)

# 2. Aprobó solo uno (diferencia simétrica)
solo_uno = parcial_1 ^ parcial_2
print("Aprobaron solo uno de los dos:", solo_uno)

# 3. Aprobó al menos uno (unión)
al_menos_uno = parcial_1 | parcial_2
print("Aprobaron al menos un parcial:", al_menos_uno)



"""EJERCICIO 8

8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe

"""
# Diccionario inicial de productos
inventario = {
    "manzanas": 10,
    "bananas": 5
}

# Pedir el nombre del producto al usuario
producto = input("Ingresá el nombre del producto: ")

# Verificar si el producto ya existe
if producto in inventario:
    print(f"El stock actual de {producto} es: {inventario[producto]}")
    
    # Agregar más unidades si existe
    agregar = int(input("¿Cuántas unidades querés agregar?: "))
    inventario[producto] += agregar
    print(f"Nuevo stock de {producto}: {inventario[producto]}")
else:
    # Si no existe, agregar nuevo producto
    nuevo_stock = int(input(f"{producto} no existe. ¿Cuántas unidades querés agregar?: "))
    inventario[producto] = nuevo_stock
    print(f"{producto} fue agregado con un stock de {nuevo_stock} unidades.")

# Mostrar inventario actualizado
print("Inventario actualizado:")
print(inventario)


"""EJERCICIO 9

9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
Permití consultar qué actividad hay en cierto día y hora.

"""
agenda = {
    ("lunes", "9:00"): "Reunión de equipo",
    ("martes", "14:30"): "Clase de inglés",
    ("viernes", "18:00"): "Gimnasio"
}

# Pedimos al usuario que consulte un día y hora
dia = input("Ingresá el día que querés consultar: ").lower()
hora = input("Ingresá la hora (por ejemplo 14:30): ")

# Creamos la tupla (día, hora)
consulta = (dia, hora)

# Consultamos en la agenda
if consulta in agenda:
    print(f"A esa hora tenés: {agenda[consulta]}")
else:
    print("No hay ninguna actividad agendada en ese horario.")



"""EJERCICIO 10

10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores

"""

mapeo = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción"
}

# Nuevo diccionario: capitales → países
invertido = {}

for pais, capital in mapeo.items():
    invertido[capital] = pais

print("Diccionario invertido:")
print(invertido)
