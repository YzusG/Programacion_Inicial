# Funciones
def determinar_anio_bisiesto(anio):
    if(anio %4 ==0) or anio %400 == 0:
        return True
    elif anio %100 == 0:
        return False





# Programa Principal
numero = int(input("Ingrese el año que desea saber: "))
bisiesto = determinar_anio_bisiesto(numero)
if bisiesto:
    print(f"el año {numero} es bisiesto")
else:
    print("No es bisiesto")