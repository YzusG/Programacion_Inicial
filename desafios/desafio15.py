# Definicion de funcion
def convertir_temp(valor_temp, unidad_original):
    if(unidad_original == "C" or unidad_original == "c"):
        temperatura_fahrenheit = (valor_temp*(9/5))+32
        return temperatura_fahrenheit
    elif( unidad_original == "F" or unidad_original == 'f'):
        temperatura_celsius = (valor_temp-32)*5/9
        return temperatura_celsius

# Programa principal
print()
temperatura = float(input("Ingrese la temperatura: "))
unidad = input("Ingrese la unidad de la temp: ")
print()

match unidad:
    case "c" | "C":
        temp_convertida = convertir_temp(unidad_original=unidad, valor_temp=temperatura)
        print(f"La temperatura en F es: {temp_convertida:.2f}")
    case 'F'| 'f':
        temp_convertida = convertir_temp(unidad_original=unidad, valor_temp=temperatura)
        print(f"La temperatura en C es: {temp_convertida:.2f}")
    case _:
        print("Unidad no valida")