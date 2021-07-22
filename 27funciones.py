##Determinar si nuestra funcion es PAR o IMPAR
num = int(input("Ingrese el valor a comprobar = "))

def reconocer(valor):
    if valor % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")

reconocer(num)
