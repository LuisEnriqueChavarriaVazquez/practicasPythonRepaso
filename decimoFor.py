numero = int(input("Ingrese un numeros entre el 0 y el 9: "))
listaMultiplos = []
contador = 0

if(numero <= 9 and numero > 0):
    print("Valor correcto")
    for i in range(0,101,1):
        if i%numero == 0:
            listaMultiplos.append(i)
else:
    print("El número no es valido")

print("Estos son los multiples de " + str(numero) + "\n")
print(listaMultiplos)
