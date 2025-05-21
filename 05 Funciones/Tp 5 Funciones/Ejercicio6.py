#Definir funciones

def tabla_multiplicar(num):
    for i in range(0, 11):
        print(f"{num} x {i} = {num * i}") 


#Programa principal

num = int(input("¿Cuál tabla de multiplicar desea ver: "))
tabla_multiplicar(num)