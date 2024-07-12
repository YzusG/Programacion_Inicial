
monto = float(input("Importe de la compra: "))
cantidad = int(input("Ingrese la cantidad de articulos: "))
descuento = 0


if monto >= 10000 and cantidad >= 5:
    descuento = monto *0.15
else:
    if cantidad < 5 and cantidad >= 3:
        descuento = monto *0.10

print(f"Importe de la compra {monto:.0f}")
print(f"Descuento Efectuados: {descuento:.0f}")
print(f"Importe a pagar: {monto - descuento:.0f}")