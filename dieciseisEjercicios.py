##Generación de listas
listaA = []
listaB = []
listaC = []
listaD = []
listaE = []

"""Todos los numeros del 0 al 10"""
for a in range(0,11):
    listaA.append(a)

"""Todos los numeros del -10 al 0"""
for b in range(-10,1):
    listaB.append(b)

"""Todos los numeros pares del 0 al 20"""
for c in range(0,21):
    if c%2 == 0:
        listaC.append(c)

"""Todos los numeros impares del -20 al 0"""
for d in range(-20,1):
    if d%2 != 0:
        listaD.append(d)

"""Todos los multiplos de 5 del 0 al 50"""
for e in range(0,51):
    if e%5 == 0:
        listaE.append(e)

print(listaA)
print(listaB)
print(listaC)
print(listaD)
print(listaE)