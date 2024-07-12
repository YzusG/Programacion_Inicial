quantity = int(input("Ingrese el importe a extrar: "))
limit = 20000

if quantity <= limit:
    print("La extracción puede realizarse")
else:
    print("La extracción debe realizarse en caja")