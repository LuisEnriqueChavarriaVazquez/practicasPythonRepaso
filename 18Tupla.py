##La tupla no puede modificarse, pero es muy parecida a la lista
tupla = (100, "Luis", [1,2,3,4], 300, False, 300)

## Obten ultimos elemento de la tupla.
print(tupla[-1])

##Numero de elementos de la tupla.
print(len(tupla))

##La posicion donde se encuentra el 300 en la tupla
print(tupla.index(300))

##Lista con los primeros tres elementos de la tupla.
nuevaLista = []
for i in range(0,3):
    nuevaLista.append(tupla[i])
print(nuevaLista)

##elemento en la posicion 4 de la tupla
print(tupla[4])

##Numero de veces que sale el 300 en la tupla
print(tupla.count(300))



