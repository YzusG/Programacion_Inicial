# Funcion
def verificar_primo(numero):
    contador = 1
    divisible = 0
    while contador <= numero:
        if(numero % contador == 0):
            divisible += 1
            contador+= 1
        else:
            contador+= 1
    if(divisible == 2):
        return True
    elif divisible > 2:
        return False

def mostrar_primo(numero):
    primo = verificar_primo(numero)
    if primo:
        print("Es un primo")
    else:
        print("No es primo")


# Programa principal
numero = int(input('Ingrese un numero: '))
mostrar_primo(numero)
