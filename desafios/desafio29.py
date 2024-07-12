def multiplos(base, limite):
    for multiplo in range (1, limite):
        if multiplo % base == 0:
            print(multiplo, end=" ")
        else:
            continue


numero = int(input("Ingrese el numero base: "))
maximo = int(input("Ingrese hasta que numero se obtendra el multiplo: "))

multiplos(numero, maximo)