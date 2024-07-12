# Funcion
def tabla_multiplicar(numero):
    """
    Calcular la tabla de multiplicar y mostrarla
    argumento: int: ingresado por el usuario n
    return: none: devuelve el resultado e imprime su iteracion
    """
    contador = 1
    while contador <= 10:
        producto = numero * contador
        print(f"{numero} x {contador} = {producto}")
        contador+=1

def tabla_multiplicar1(numero):
    base = 1
    while base <= numero:
        contador = 1 #Aqui cambia si esta afuera no influye en el bucle mas interno sino que solo lo toma el bucle externo
        while contador <= 10:
            producto = base * contador
            print(f"{base} x {contador} = {producto}")
            contador+=1
        base += 1
        





# Programa
print()
n = int(input("Ingrese un numero para obtener su tabla: "))
print(f"Tabla de multiplicar del {n}")
tabla_multiplicar1(n)