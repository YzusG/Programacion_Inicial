def separador():
    print("="*30)

def pelicula(nombre, dia, hora, sala):
    print(f"{nombre}\n{dia}\t{hora}\nSala:{sala}")

def tickets(cantidad, valor, por_descuento):
    print(f"Valor de la entrada: $ {valor}")
    print(f"Cantidad de entradas: {cantidad}")
    if cantidad >= 5:
        ticket = (cantidad *valor) * (por_descuento)/100
        print(f"Valor del Ticket: $ {ticket}")
    else:
        ticket = valor *cantidad
        print(f"Valor del Ticket: $ {ticket}")

#Programa Principal
print(); print()

nombre   = input("Ingrese la pelicula: ")
dia      = input("Ingrese dia con fecha: ")
hora     = input("Ingrese la Hora de la funcion:")
sala     = input("Ingrese la sala que desea: ")
cantidad = int(input("Cuantas entradas desea: "))

separador()
pelicula(nombre,dia,hora,sala)
separador()
tickets(cantidad, 5000, 15)