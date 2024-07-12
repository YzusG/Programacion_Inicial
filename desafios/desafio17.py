'''
print([1] Suma.)
print([2] Resta.)
print([3] Multiplicación.)
print([4] División)
print([5] Potencia de los números.)
print([6] Verificar si ambos números )son pares.
print([7] Verificar cuál de los valores )es el mayor.
print([8] Salir)
'''
# Definicion de programas
def espaciar():
    print(); print()

def titulo():
    print('*'*30)
    print("Calcular de Graterol")
    print('*'*30)
    print()

def mostrar_menu():
    print("[1] Suma.")
    print("[2] Resta.")
    print("[3] Multiplicación.")
    print("[4] División")
    print("[5] Potencia de los números.")
    print("[6] Verificar si ambos números son pares.")
    print("[7] Verificar cuál de los valores es el mayor.")
    print("[8] Salir")

def sumar(numero_1, numero_2):
    suma = numero_1 + numero_2
    return suma

def restar(numero_1, numero_2):
    resta = numero_1 - numero_2
    return resta

def multiplicar(numero_1, numero_2):
    producto = numero_1 * numero_2
    return producto

def dividir(numero_1, numero_2):
    division = numero_1 / numero_2
    return division

def potencia(numero_1, numero_2):
    pot = numero_1 ** numero_2
    return pot

def validar_par(numero_1, numero_2):
    if(numero_1 % 2 == 0) and numero_2 %2 ==0:
        print("los numeros son pares")
    else:
        print("Uno de los dos numeros o ambos no son pares")

def verificar_el_mayor(numero_1, numero_2):
    mayor= 0
    if numero_1 > numero_2:
        mayor = numero_1
        print(f"El mayor es {mayor}")
    elif numero_1 == numero_2:
        print("ninguno es mayor")
    else:
        mayor = numero_2
        print(f"El mayor es {mayor}")


# Programa Principal
bandera = True
espaciar()
while bandera:
    titulo()
    mostrar_menu()
    op = input("Ingrese la operacion a realizar: ")
    espaciar()
    match op:
        case '8':
            print("Gracias por usar la calculadora")
            bandera = False
        case "1":
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
            total = sumar(num1, num2)
            print(f"El total es: {total:.2f}")
        case "2":
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
            total = restar(num1, num2)
            print(f"El total es: {total:.2f}")
        case "3":
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
            total = multiplicar(num1, num2)
            print(f"El total es: {total:.2f}")
        case "4":
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
            if num1 == 0 or num2 == 0:
                print("Syntax error: No se puede dividir entre 0")
            else:
                total = dividir(num1, num2)
                print(f"El total es: {total:.2f}")
        case "5":
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
            total = potencia(num1, num2)
            print(f"El total es: {total:.2f}")
        case "6":
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
            validar_par(num1,num2)
        case "7":
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
            verificar_el_mayor(num1,num2)