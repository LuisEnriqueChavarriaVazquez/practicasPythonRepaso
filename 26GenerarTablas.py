print("Bienvenido a nuestro generador de tablas de multiplicar")
multiplo = int(input("Ingrese el valor de la tabla de multiplicar"))

def multiplicar(multiplo):
    for i in range(0,11):
        print(str(multiplo) + " x " + str(i) + " = " + str(multiplo*i))
        
    multiplicar(multiplo)

