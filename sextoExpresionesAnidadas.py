nombre = input("Escriba su nombre: ")
edad = int(input("Escriba su edad: "))

if(nombre != "****" and edad > 10 and edad < 18 and len(nombre) >= 3 and len(nombre) < 10):
    expresion = "Cumple"
    print(expresion)
else:
    print("No cumple")
