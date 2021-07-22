##Dada dos lista debemos unirlas con elementos repetidos, pero en la nueva lista ningun elementos puede repetirse.

listaUno = ["H","O","L","A","M","U","N","D","O"]
listaDos = ["H","O","L","A","L","U","I","S"]
listadoFinal = []

for elemUno in listaUno:
    if(elemUno in listaDos):
        listadoFinal.append(elemUno)

print("Hemos terminado revisión de repetición")
##Quita repeticiones
print("El listado final es el siguiente.")
print(list(set(listadoFinal)))



        