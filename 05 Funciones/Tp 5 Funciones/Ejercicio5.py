#Definir funciones
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

#Programa principal
if __name__ == "__main__":
    segundos =  float(input("Ingrese los segundos: "))
    horas = segundos_a_horas(segundos)
    print(f"{segundos} segundos equivalen a {horas:.2f} horas")