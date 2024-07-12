#Area de un triangulo
def area_triangulo(longitud, altura):
    return (longitud*altura)/2

base = int(input("Ingrese la base:"))
altura = int(input("Ingrese la altura:"))

area = area_triangulo(base, altura)

print(f"El area del triangulo es: {area:.2f}")