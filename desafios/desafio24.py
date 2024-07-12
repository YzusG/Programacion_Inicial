# Funcion
def secuencia_fibonacci(numero):
    """
    Genera los primeros numeros de la secuencia de fibonacci
    Argumento: cantidad de Numeros (int)
    return: Imprime en consola la secuencia (none)
    nota: Una solucion es que el contador empiece en 3 para cortar la secuencia, y en un print por fuera se muestre los dos primeros numeros (Para asi mostrar el cero)
    """
    contador = 3
    num1 = 0
    num2 = 1
    print(f"{num1} {num2}", end=" ")
    while contador <= numero:
      fibonacci = num1 + num2
      print(fibonacci, end=" ")
      num1 = num2
      num2 = fibonacci
      contador += 1


# Programa
numero = int(input("Ingrese el numero para la secuencia: "))
secuencia_fibonacci(numero)
