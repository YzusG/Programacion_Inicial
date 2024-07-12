#Definicion de funcion
def convertir_distancia(distancia_km):
    factor_conversor = 1.60934
    return distancia_km*factor_conversor

#Programa princial
print()
distancia = float(input("Ingrese que distancia (Km) desea convertir:"))

distancia_millas = convertir_distancia(distancia)

print(f"La distancia de {distancia:.2f} km", end=" ")
print(f"en millas es: {distancia_millas}")
# print(f"la distancia en millas es: {distancia_millas}")