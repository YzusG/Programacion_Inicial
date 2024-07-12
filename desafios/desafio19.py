#funcion
def determinar_mayor(numero1, numero2, numero3):
    mayor = 0
    if numero1 > numero2 and numero1 > numero3:
        mayor = numero1
        print(f"El numero mayor es {mayor}")
    elif numero2 > numero1 and numero2> numero3:
        mayor = numero2
        print(f"El numero mayor es {mayor}")
    else:
        mayor = numero3
        print(f"El numero mayor es {mayor}")

# Programa Principal
num1 = float(input("Introduzca un numero: "))
num2 = float(input("Introduzca un numero: "))
num3 = float(input("Introduzca un numero: "))

determinar_mayor(num1 ,num2 ,num3)