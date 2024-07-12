#UN algoritmo que permita la entrada
#a un juego de un parque de diversiones
#solo si pagamos y somos mayores de 18 años

print();print();print()

edad = int(input("Ingrese su edad: "))
pago = True #pago la entrada
'''
if edad >= 18:
    if pago:
        print("Puede pasar")
'''
if edad >= 18 & pago:
    print("Admitido")
else:
    print("No puede entrar")


print(); print (); print()