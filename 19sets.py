grupo = {"Ana","Miguel","Ramón","Marta","Eric","David","Blanca", "Mario", "Andres"}

#Elimina a los usuarios Mario, Miguel y Ramón
grupo.remove("Mario")
grupo.remove("Miguel")
grupo.remove("Ramón")

#Imprime el nuevo listado
print(list(grupo))

#Agregamos nuevo elementos a nuestro set(conjunto)
grupo.add("Luis Enrique Chavarria Vázquez")
print(list(grupo))
