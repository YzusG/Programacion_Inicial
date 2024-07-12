codProduct = input("Ingrese el codigo del Producto: ").upper()


if codProduct[0]== "A":
    print("Su producto es un Electronico")
elif codProduct[0] == "B":
    print("Su producto es Ropa")
elif codProduct[0] == "C":
    print("Su producto es Alimenticio")
else:
    print("Su producto es desconocido")

'''match codProduct[0]:
    case "A":
          print("Su producto es un Electronico")
    case "B":
          print("Su producto es Ropa")
    case "C":
          print("Su producto es Alimenticio")
    case _:
            print("Su producto es desconocido")
'''