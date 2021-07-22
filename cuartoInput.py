name = input("Dame tu nombre")
surename = input("Dame tu apellido")
age = int(input("Dame tu edad"))
magicNumber = float(input("Dame un numero magico"))

cadenaFinal = name + " " + surename + ": Tu número de la suerte es el " + str(age*magicNumber) 
print(cadenaFinal)