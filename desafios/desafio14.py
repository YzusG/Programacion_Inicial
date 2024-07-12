
# Definicion de la funcion
def calcular_imc(peso_kg,altura_m):
    imc = (peso_kg)/((altura_m)*altura_m)
    return imc

# Programa principal
peso = float(input("Ingrese su peso [Kg]: "))
altura = float(input("Ingres su altura [m]: "))

imc = calcular_imc(altura_m=altura, peso_kg=peso)

print(f"Su Indice de Masa Corporal es: {imc:.2f}")