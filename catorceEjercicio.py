##Ingresa n numero de valores, luego saca la media aritmetica.

totalNumeros = int(input("Dame el total de números: "))
listaNumeros = []
sumaTotal = 0

for i in range(1,totalNumeros+1):
    nuevoValor = int(input("Dame el valor " + str(i) + ": "))
    listaNumeros.append(nuevoValor)

for elementoListaNumeros in listaNumeros:
    sumaTotal += elementoListaNumeros

print("El promedio es de " + str(sumaTotal/totalNumeros))
