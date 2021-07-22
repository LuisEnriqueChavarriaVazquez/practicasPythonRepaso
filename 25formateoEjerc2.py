##Debemos ingresar un número y descomponerlo en valores más pequeños
"""
3456 ==> 3000 0400 0050 0006
"""

numero = int(input("Ingresa el valor para descomponerlo = "))
numeroTexto = str(numero)
numeroLargo = len(str(numero))

def millon(numero):
    valor = numero[-7]
    return int(valor)

def cienK(numero):
    valor = numero[-6]
    return int(valor)

def diezK(numero):
    valor = numero[-5]
    return int(valor)

def unK(numero):
    valor = numero[-4]
    return int(valor)

def cien(numero):
    valor = numero[-3]
    return int(valor)

def diez(numero):
    valor = numero[-2]
    return int(valor)

def unidad(numero):
    valor = numero[-1]
    return int(valor)

def descomponer():
    if numeroLargo == 1:
        print(f"Unidades {unidad(numeroTexto):07d}")
    elif numeroLargo == 2:
        print(f"Unidades {unidad(numeroTexto):07d}")
        print(f"Decenas {diez(numeroTexto):07d}")
    elif numeroLargo == 3:
        print(f"Unidades {unidad(numeroTexto):07d}")
        print(f"Decenas {diez(numeroTexto):07d}")
        print(f"Centenas {cien(numeroTexto):07d}")
    elif numeroLargo == 4:
        print(f"Unidades {unidad(numeroTexto):07d}")
        print(f"Decenas {diez(numeroTexto):07d}")
        print(f"Centenas {cien(numeroTexto):07d}")
        print(f"Millares {unK(numeroTexto):07d}")
    elif numeroLargo == 5:
        print(f"Unidades {unidad(numeroTexto):07d}")
        print(f"Decenas {diez(numeroTexto):07d}")
        print(f"Centenas {cien(numeroTexto):07d}")
        print(f"Millares {unK(numeroTexto):07d}")
        print(f"Decenas de millares {diezK(numeroTexto):07d}")
    elif numeroLargo == 6:
        print(f"Unidades {unidad(numeroTexto):07d}")
        print(f"Decenas {diez(numeroTexto):07d}")
        print(f"Centenas {cien(numeroTexto):07d}")
        print(f"Millares {unK(numeroTexto):07d}")
        print(f"Decenas de millares {diezK(numeroTexto):07d}")
        print(f"Centenas de millares {cienK(numeroTexto):07d}")
    elif numeroLargo == 7: 
        print(f"Unidades {unidad(numeroTexto):07d}")
        print(f"Decenas {diez(numeroTexto):07d}")
        print(f"Centenas {cien(numeroTexto):07d}")
        print(f"Millares {unK(numeroTexto):07d}")
        print(f"Decenas de millares {diezK(numeroTexto):07d}")
        print(f"Centenas de millares {cienK(numeroTexto):07d}")
        print(f"Millones {millon(numeroTexto):07d}")
    else:
        print("Valor no soportado")

descomponer()