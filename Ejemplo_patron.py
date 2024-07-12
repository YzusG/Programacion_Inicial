"""
Aqui establecemos un cuadrado, empezamos como la primera fila
el bucle externo sera hasta la fila 5 e iniciamos en la primera
columna, en el bucle interno el de las columnas va a imprimir el
"* " y va a incrementar la columna hasta 5, luego sale del bucle
incrementa la fila y vuelve a saltar a la columna 1 pero en la siguiente fila, como una matriz
"""


fila = 1
while fila <= 5:
    columna = 1
    while columna <= 5:
        print("* ", end="")
        columna = columna + 1
    print()
    fila = fila + 1


"""
Aqui es importante evaluar los limites usando el OR, ya evaluar
cuando son iguales a 1 y 5, evaluamos si el valor de fila es MENOR
a 5 y de alli evaluamos el valor de columna si es IGUAL a 1 o 5
imprime el * sino es evaluamos si es mayor a 1 OR menor a 5 que lo
deje en blanco

"""
fila = 1
while fila <= 5:
    columna = 1
    while columna <= 5:
        if fila ==1 or fila == 5:
            print( "* ", end="")
        elif fila <5: 
            if columna == 1 or columna ==5:
                print("* ", end="") 
            elif columna > 1 or columna <5:
                print("  ", end="")
        columna = columna + 1
    print()
    fila = fila + 1

fila = 1
while fila <= 5:
    columna = 1
    while columna <= 5:
        if fila == columna:
                print("* "*fila)
        columna += 1
    fila += 1