def tabla_multiplicar():
    numero = int(input("Ingrese el numero de la tabla que desea: "))
    contador = 1
    while contador <= 10:
        print (f"{numero} x {contador} = {numero*contador}")
        contador+=1

tabla_multiplicar()