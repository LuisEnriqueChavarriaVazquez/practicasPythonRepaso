"""Formatea los siguientes valores para mostrar el resultado indicador"""

## "Hola Mundo" ==> Alineado a la derecha en 20 caracteres
## "Hola Mundo" ==> Truncamiento en el cuarto carácter (indice 3)
## "Hola Mundo" ==> Alineamiento al centro en 20 caracteres con truncamiento en el segundo carácter (índice 1)
## 150 ==> Formateo a 5 números enteros rellenados con ceros
## 7887 ==> Formateo a 7 números enteros rellenados con espacios
## 20.02 ==> Formateo a 3 núemros enteros y 3 números decimales
textoUno = "Hola Mundo"
numUno = 150
numDos = 7887
numTres = 20.02

print(f"{textoUno:>20}") ##Punto uno
print(f"{textoUno:.4}") ##Punto dos
print(f"{textoUno:^20}") ##Punto tres
##Formato de los números
print(f"{numUno:05d}") ##Punto cuatro
print(f"{numDos: 7d}") ##Punto cuatro
print(f"{numTres:07.3f}") ##Punto cuatro
