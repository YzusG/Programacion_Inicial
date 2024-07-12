# Funcion
def factorial(numero):
    contador = 1
    resultado = 1
    while contador <= numero:
        resultado = resultado * contador
        contador += 1
    return resultado

# Programa
print()
n = int(input("Ingrese el numero a calcular el factorial:"))
total = factorial(n)
print(f"El factorial de {n} es {total}")