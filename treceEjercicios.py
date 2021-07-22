##Programa que sume todos los pares del 0 al 100
suma = 0

for i in range(0,101):
    if(i%2 == 0):
        suma += i

print(suma)