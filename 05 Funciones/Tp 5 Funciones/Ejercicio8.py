#Definir funciones
def calcular_imc(peso, altura):
    IMC = peso / (altura**2)
    return IMC


#Programa principal
peso = float(input("Ingrese su peso en kilogramos: "))
altura =  float(input("Ingrese su altura en metros: "))

resultado_imc = calcular_imc(peso,altura)
print(f"\nSu índice de Masa Corporal (IMC) es: {resultado_imc:.2f}")