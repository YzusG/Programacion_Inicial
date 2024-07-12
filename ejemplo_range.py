# definimos la lista de numeros enteros
numeros =[10,20,40,50]

# Inicializamos la variable que usaremos para mantener la suma
suma_total  =0

# Inizializamos la variable para almacenar el numero mas alto
numero_maximo = numeros[0]

# Aqui usaremos la iteracion

for numero in range(numeros.index(10), numeros.count):
    suma_total += numero
    if (numero > numero_maximo):
        numero_maximo = numero

print(f"La suma total es: {suma_total}")
print(f"El numero maximo es: {numero_maximo}")