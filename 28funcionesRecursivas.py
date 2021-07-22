
numero = int(input("Dame algun valor para la suma = "))

def sumatorio(valor):
    print("Inicio con el valor",str(valor))
    if valor > 0:
        valor = valor + sumatorio(valor - 1)
    print("Final con el valor",str(valor))
    return valor

def multi(valor):
    print("Inicio con el valor",str(valor))
    if (valor > 1):
        valor = valor * multi(valor-1)
    print("Fin con el valor",str(valor))
    return valor

print(sumatorio(numero))
print(multi(numero))