#definir funciones

def saludar_usuario(nombre):
    print (f"Hola {nombre}")

#programa principal

if __name__ == "__main__":
    nombre = input("¿Cuál es tu nombre? ")
    saludar_usuario(nombre)