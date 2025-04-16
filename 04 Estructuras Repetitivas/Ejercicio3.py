#Escribe un programa que sume todos los números enteros 
# comprendidos entre dos valores dados por el usuario, 
# excluyendo esos dos valores.

valor_uno = int(input("Ingresa el primer valor "))
valor_dos = int(input("Ingresa el segundo valor "))

contador = 0

for i in range((valor_uno+1),valor_dos):
    contador += i

print(contador)