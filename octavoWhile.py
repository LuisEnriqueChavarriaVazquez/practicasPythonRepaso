numero = int(input("Dame cualquier numero: "))

while numero%5 != 0:
    numero += 1
    if numero%5 == 0:
        print("Valor del número multiplo de 5 es " + str(numero))
        break

