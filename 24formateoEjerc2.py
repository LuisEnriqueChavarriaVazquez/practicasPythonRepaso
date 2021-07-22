##Vamos a imprimir una celda con * con valores del 0 al 9
while True:
    texto = " * "
    fila = int(input("Ingrese el número de filas = ")) #Horizontal
    columna = int(input("Ingrese el número de columnas = ")) #Vertical

    if fila > 9 or columna > 9 or fila < 0 or columna < 0:
        print("Los valores fuera del limite establecido")
        fila = int(input("Ingrese el número de filas = ")) #Horizontal
        columna = int(input("Ingrese el número de columnas = ")) #Vertical

    for i in range(0,1):
        texto = texto * fila

    for j in range(0,columna):
        print(texto)
