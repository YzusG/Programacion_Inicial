'''
Desafio 1
Datos personales en formato de tarjeta
'''

name = input("Ingrese nombre de titular:").capitalize()
lastname = input("Ingrese el apellido:").upper()
year = input("Año de nacimiento:")
city = input("Ciudad de Residencia:")
age = 2024 - int(year)
titulo = "DATOS PERSONALES"

print(); print()

print(titulo.center(100, "*")); print()

print("-".center(100,"-"))
print("|", f"Apellido y nombre: {lastname}, {name}")
print("|", f"Año de nacimiento: {year}")
print("|", f"Correo electronico: {lastname.lower()}{name.lower()}.{year}@empresa.com.ar")
print("|", f"Ciudad: {city}")
print("|", f"Edad: {age} años")

print();print("-".center(100,"-"))