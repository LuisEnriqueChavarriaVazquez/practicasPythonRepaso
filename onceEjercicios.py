##Hacer un menu simple
num1 = 1
num2 = 2

while(True):
    print("//////////////////////////////////")
    print("Suma de los números")
    print("Resta de los números")
    print("Multiplicación de los números")
    print("//////////////////////////////////" + "\n")

    opcion = input("Ingrese una opcion: ")
    if(opcion == "1"):
        print("La suma de los números es " + str(num1 + num2))
    if(opcion == "2"):
        print("La resta de los números es " + str(num2 - num1))
    if(opcion == "3"):
        print("La multi de los números es " + str(num1 * num2))
    if(opcion == "4"):
        print("Adios")
        break
    else:
        print("Ingrese un valor valido")
    