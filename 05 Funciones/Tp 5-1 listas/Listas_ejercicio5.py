#Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

# Explicación: 

""" En la primer línea de código está creada la lista 'numeros' que tiene 5 elementos numéricos, enteros.
    En la segunda línea se busca el número más grande de la lista (con el método max(numeros)).
    Una vez que se obtiene ese valor, se elimina (usando remove()) de la lista 'numeros'.

    Por último, se imprime por pantalla la lista 'numeros' sin el número más grande.
"""
