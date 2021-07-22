##Ingresa un numero impar y repite hasta que el usuario lo haga

numeroImpar = 0
while numeroImpar%2 == 0:
    numeroImpar = int(input("Dame algun número impar: "))
    if(numeroImpar%2 != 0):
        print("El número impar es el siguiente " + str(numeroImpar))
        break
    else:
        print("Debes ingresar un número impar")