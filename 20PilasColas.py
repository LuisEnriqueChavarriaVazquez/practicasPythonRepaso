usuarios = {"Marta", "David", "Elvira", "Juan", "Marcos"}
administradores = {"Juan", "Marta"}
contador = 0
contadorAdmins = 0

administradores.remove("Juan") ##Podemos usar discard tambien
administradores.add("Marcos")
administradores.add("Luis")
administradores.discard("Luis")

"""Discard lo que hace es que cuando borra si el elemento no
esta entonces NO HAY ERROR // Con delete si no hay elemento
nos da error."""

print("\nListado de usuarios. \n")
for usuario in usuarios:
    contador += 1
    print(usuario + " es el usuario número " + str(contador))

print("\nListado de admins.\n")
for admin in administradores:
    contadorAdmins += 1
    if admin in usuarios:
        print(admin + " es el admin y usuario número " + str(contadorAdmins))
    else:
        print(admin + " es el admin número " + str(contadorAdmins))

