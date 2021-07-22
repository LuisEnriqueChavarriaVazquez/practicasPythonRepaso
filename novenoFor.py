
##Recorrido simplemente sumando sin una lista
for i in range(10):
    print("Valor " + str(i))

##Recorrido de la lista pero con un indice
numeros = [1,2,3,4,5,6,7,8,9,10]
for indice,numero in enumerate(numeros):
    print(numeros[indice] * 10)

##Recorrido de la lista
for numero in numeros:
    print("Valor en la lista " + str(numero))