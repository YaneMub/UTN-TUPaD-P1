import Ejercicio2

#definir funciones

def informacion_personal(nombre, apellido, edad, residencia):
    mensaje = f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}."
    Ejercicio2.saludar_usuario(mensaje)

#programa principal

nombre = input("¿Cuál es tu nombre? ")    
apellido = input("¿Cuál es tu apellido? ") 
edad = input("¿Cuántos años tienes? ") 
residencia = input("¿Dónde vives? ") 

informacion_personal(nombre, apellido, edad, residencia)