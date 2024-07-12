def tabla_multiplicar(num):
    contador = 1
    while contador <= 10:
        producto = contador * num
        print (f"{contador} x {num} = {producto}")
        contador+= 1

#Programa principal
print(); print(); print()
print("Generador de Tablas para Ciencias Graterol & Asociados")
print(); print(); print()
bandera = True
while bandera:
    numero = int(input("Ingrese que tabla desea: ")); print()
    if numero >10:
        print("Numero fuera del rango, solo se hacen tablas del 0 al 10")
    else:
        tabla_multiplicar(numero)
        bandera = False
print(); print(); print()