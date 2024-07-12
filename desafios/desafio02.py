client = input("Razon Social: ")
address = input("Domicilio: ")
quantity = int(input("Cantidad:"))
description = input("Descripcion del producto: ")
price = int(input("Precio Unitario: "))
iva = 0.21
subtotal = price * quantity



print(),print()
print("DATOS DEL CLIENTE:")
print("Cantidad\tDescripcion\tP.U\t\tSubtotal")
print(f"{quantity}\t\t{description}\t\t${price}\t\t{subtotal}")
print()
print("CALCULOS ADICIONALES:")
print(f"IVA({iva*100}%):\t\t${subtotal*iva+subtotal}")
print("Descuento Aplicado:\t-$6000,00")
print("TOTAL A PAGAR:")
print(f"Total con IVA:\t\t${subtotal*iva}")
print("Descuento aplicado:\t-$6000,00")
print(f"Total a Pagar:\t\t${subtotal*iva-6000+subtotal}");print()

print("FORMA DE PAGO:")
print(f"1.CONTADO:\t\t\t${subtotal*iva-6000+subtotal}")
print(f"2. 3 CUOTAS(15% de interes):\t{(subtotal*iva-6000+subtotal)*0.15}")
print(f"3.6 CUOTAS (25% de interes):\t{(subtotal*iva-6000+subtotal)*0.25}"); print()
print("¡Gracias por su compra!")