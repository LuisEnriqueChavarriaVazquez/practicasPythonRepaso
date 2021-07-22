cadenaUno = input("Ingrese un texto uno: ")
cadenaDos = input("Ingrese un texto dos: ")
resultado = 0

if(len(cadenaUno) > len(cadenaDos)):
    resultado = 1
    print(resultado)
elif(len(cadenaUno) < len(cadenaDos)):
    resultado = 2
    print(resultado)
else:
    resultado = 0
    print(resultado)
