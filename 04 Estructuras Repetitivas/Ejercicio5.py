#Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. 
# Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
aleatorio = random.randint(0,9)

numero = float("inf")
cantidad_Intentos = 0

while numero != aleatorio:
    numero = int(input("Elija un número entre 0 y 9..."))
    cantidad_Intentos += 1

    if numero != aleatorio:
        print("¡Intentalo de nuevo!")
    elif numero == aleatorio:
        print(f"¡Eso es!, adivinaste el número en el intento {cantidad_Intentos}")

