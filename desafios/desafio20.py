from math import pi

# Funciones
def mostrar_menu():
    '''
    Esta funcion muestra el menu del programa de geometria.

    Nota: Se le agrego la opcion [5] para lograrlo en bucle
    '''
    print("[1] Hallar el área de un cuadrado")
    print("[2] Hallar el área de un rectángulo")
    print("[3] Hallar el área de un triángulo")
    print("[4] Hallar el área de un círculo")
    print("[5] Salir")

def hallar_area_cuadrado():
    '''
    Calcula el area de un cuadrado

    Argumento(): None

    return (int): Regrese el valor del area
    '''
    lado = float(input("Ingrese el lado: "))
    return lado**2

def hallar_area_rectangulo():
    '''
    Calcula el area de un rectangulo

    Argumento(): None

    return (int): Regrese el valor del area
    '''
    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura: "))
    return base * altura

def hallar_area_triangulo():
    '''
    Calcula el area de un triangulo

    Argumento(): None

    return (int): Regrese el valor del area
    '''
    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura: "))
    return (base * altura)/2

def hallar_area_circulo():
    '''
    Calcula el area de un ciruclo

    Argumento(): None

    return (int): Regrese el valor del area
    '''

    radio = float(input("Ingrese el radio:"))
    return (pi*radio**2)

# Programa
controlador = True
while controlador:
    mostrar_menu()
    op = input("Ingrese su opcion: ")
    match op:
        case "1":
            area = hallar_area_cuadrado()
            print(f"El area es {area:.2f}")
        case "2":
            area = hallar_area_rectangulo()
            print(f"El area es {area:.2f}")
        case "3":
            area = hallar_area_triangulo()
            print(f"El area es {area:.2f}")
        case "4":
            area = hallar_area_circulo()
            print(f"El area es {area:.2f}")
        case "5":
            controlador = False
            # print(help(hallar_area_circulo))