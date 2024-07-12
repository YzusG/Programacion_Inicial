# def tabla_multiplicar():
#     n = int(input("Ingrese la tabla que desea obtener: "))
#     for base in range (1, 11):
#         print(f"{n} x {base} = {base * n}")


# tabla_multiplicar()

def tabla_multiplicar2():
    n = int(input("La tablas de multiplicar que desea es hasta: "))
    for n in range (1, n+1):
        for base in range (1, 11):
            print(f"{n} x {base} = {base * n}")

tabla_multiplicar2()