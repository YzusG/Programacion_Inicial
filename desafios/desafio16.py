# Definicion de programa
def calcular_volumen_cilindro(radio,altura):
    volumen = (3.1415926*radio*radio)*altura
    print(f"El volumen del cilindro es: {volumen:.2f}")

# Programa principal
print()
base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))
print()
calcular_volumen_cilindro(base,altura)