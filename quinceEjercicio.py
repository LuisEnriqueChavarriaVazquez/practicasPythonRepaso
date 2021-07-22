##Pedir un valor del 0 al 9 y comprobar si se encuentra dentro de la lista
numero = -1
listaValores = [0,3,5,7]


while(numero > 9 or numero < 0):
    numero = int(input("Dame un valor del 0 al 9"))
    if(numero > 0 and numero < 9):
        print("Valor correcto")
        if numero in listaValores:
            print("▄▄ El valor se encuentra en la lista")
        else:
            print("▄▄ El valor se encuentra fuera de la lista")
        break
    else:
        print("Rango inadecuado")
