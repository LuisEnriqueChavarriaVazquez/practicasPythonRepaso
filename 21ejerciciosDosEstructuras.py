##Durante el desarrollo de un videojuego se te encarga configurar y balancear
##cada clase de personaje jugable. Paritendo que la estadisitica base es dos
##,debes cumplir las siguientes condiciones.

"""El caballero tiene doble de vida y defensa que un guerrero"""
"""El guerrero tienen el doble de ataque y alcance que un caballero"""
"""El arquero tienen la misma vida y ataque que un guerrero, pero la mitad de su defensa y el doble de su alcance"""
"""Muestra como quedan las propiedades de los tres personajes."""

caballero = {"vida":2,"ataque":2,"defensa":2,"alcance":2}
guerrero = {"vida":2,"ataque":2,"defensa":2,"alcance":2}
arquero = {"vida":2,"ataque":2,"defensa":2,"alcance":2}

#Primer punto
caballero['vida'] = guerrero['vida'] * 2
caballero['defensa'] = guerrero['defensa'] * 2

#Segundo punto
guerrero['ataque'] = caballero['ataque'] * 2
guerrero['defensa'] = caballero['alcance'] * 2

#Tercer punto
arquero['ataque'] = guerrero['ataque']
arquero['vida'] = guerrero['vida']
arquero['defensa'] = guerrero['defensa'] / 2
arquero['alcance'] = guerrero['alcance'] * 2

#Mostrar propiedades de nuestros personajes
print("Datos del caballero \n")
print("Vida " + str(caballero['vida']))
print("Ataque " + str(caballero['ataque']))
print("Defensa " + str(caballero['defensa']))
print("Alcance " + str(caballero['alcance']))

print("\nDatos del guerrero \n")
print("Vida " + str(guerrero['vida']))
print("Ataque " + str(guerrero['ataque']))
print("Defensa " + str(guerrero['defensa']))
print("Alcance " + str(guerrero['alcance']))

print("\nDatos del arquero \n")
print("Vida " + str(arquero['vida']))
print("Ataque " + str(arquero['ataque']))
print("Defensa " + str(arquero['defensa']))
print("Alcance " + str(arquero['alcance']))
