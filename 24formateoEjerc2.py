##Vamos a imprimir una celda con * con valores del 0 al 9
filas = -1
columnas = -1
if filas > 9 and filas < 0:
    print("Ingrese valores entre el 9 y el 0 para la fila")
    filas = int(input("Número de filas"))
    if columnas > 9 and columnas < 0:
        print("Ingrese valores entre el 9 y el 0 para la columna")
        columnas = int(input("Número de columnas"))


