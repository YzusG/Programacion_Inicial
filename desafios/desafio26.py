# Funcion
def suma_enteros():
    n = int(input("Ingrese un numero entero: "))
    suma= 0
    for n in range(1, n+1):
        suma += n
    print(f"la Suma es: {suma}")

suma_enteros()