#[1] Crear Cuenta
#[2] Consultar Saldo
#[3] Deposito
#[4] Extraccion
#[5] Pagos
#[6] Transferencias
#[S] Salir

# ------------------------------------
#Definimos las funciones a utilizar
# ------------------------------------
def mostrar_menu():
    print()
    print('-'*30)
    if not existe_usuario: #Aqui hacemos lo mismo pero con la diferencia que una vez creado el usuario ya no muestra el cartel de la primera opcion
        print('[1] Crear Cuenta')
    print('[2] Consultar Saldo')
    print('[3] Deposito')
    print('[4] Extraccion')
    print('[5] Pagos')
    print('[6] Transferencias')
    print('[S] Salir')
    print()


def crear_cuenta():
    # global nombre, saldo esto ya no es una buena practica, antes se hacia y se puede conseguir pero ya no es mas una buena practica
    print('-'*30)
    nombre = input('Ingrese el nombre: ')
    saldo = float(input('Ingrese el saldo: '))
    print()
    print(f'Bienvenido {nombre}')
    return nombre, saldo

def consultar_saldo(nom, importe):
    print('-'*30)
    print()
    print(f'Titular: {nom}')
    print(f'Su saldo es: ${importe:.2f}')


def depositar(saldo_anterior):
    # global saldo
    print('-'*30)
    print(f"Saldo actual: $ {saldo_anterior:.2f}")
    importe = float(input('Monto a depositar: '))
    saldo_actual = importe + saldo_anterior
    print(f"Saldo actual: ${saldo:.2f}")
    print()
    return saldo_actual


def extraccion(saldo_anterior):
    print('-'*30)
    print(f"Saldo actual: $ {saldo_anterior:.2f}")
    retiro = float(input('Monto a retirar: '))
    if retiro <= saldo:
        saldo_nuevo = saldo_anterior - retiro
        print(f"Saldo Actualizado: ${saldo_nuevo:.2f}")
        return saldo_nuevo
    else:
        print('Saldo insuficiente')
        return saldo_anterior

def error_cuenta():
    print()
    print('La cuenta ya existe')
    print()
# ------------------------------------
# Programa principal
# ------------------------------------
condicion = True
nombre = ""
saldo = 0
existe_usuario = False


while condicion:
   mostrar_menu()
   opcion = input('Elija una opcion: ')

   match opcion:
        case '1': #Crear la cuenta
           if  not existe_usuario: #Aqui verificamos que si existe el usuario
            nombre, saldo = crear_cuenta()
            existe_usuario = True
           else:
               error_cuenta() #Aqui llevamos el codigo a una funcion
        case '2': #Consultar saldo
            consultar_saldo(nombre, saldo)
        case '3': #Depositar
            saldo = depositar(saldo)
        case '4': #Retirar
            saldo = extraccion(saldo)
        # case 5:

        # case 6:

        case 'S' | 's': # Salir
            condicion = False
            print('Retire la tarjeta. Adios')