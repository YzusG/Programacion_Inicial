#UN algoritmo que permita la entrada
#a un juego de un parque de diversiones
#solo si pagamos y somos mayores de 18 años

print();print();print()

edad = int(input("Ingrese su edad: "))
pago = input("Pago la entrada? [s/n]: ")
pago = pago.upper()


'''
if edad >= 18:
    if pago:
        print("Puede pasar")
'''
if edad >= 18 and pago == "S":
    print("Admitido")
else:
    print("No puede entrar")


print(); print (); print()