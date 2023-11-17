numero1 = 10  # entero
numero2 = 100.46  # float
nombre = "Belen"  # string
apellido = "Arista"
es_mayor = True  # mayuscula T
es_menor = False  # Mayuscula F

print(nombre, numero1, numero2)

print("Hola " + nombre + "  " + apellido + "saludos")

# f string
# permite colocal variables dentro de un string
print(f"hola mi nombre es {nombre} {apellido} , saludos ")
print(nombre + str(numero1))
print(numero2 + numero1)

print("=== LISTAS ===")
teams = ["barcelona", "Real Madrid", "PSG",
         "Boca Jr", ["Messi", "MBAPE", "CR7"]]
print(teams[4][2])

tv_shows = ["spiderman", "the bing bang theory",
            "moises", ["breaking bad", "batman"]]
print(tv_shows)

tv_shows.append("black mirror")
print(tv_shows)

# extend() Une una lista con otra. en JS es concat

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend(l2)
print(l1)

# remove() recibe un valor y elimina el primer item de la lista que concuerde con ese valor
tv_shows.remove("spiderman")
print(tv_shows)

# pop() por default elimina el ultimo y sino recibe un indice

# tv_shows.pop(1)
# print(tv_shows)

tv_shows[2].pop(0)
print(tv_shows)

# index()
print(tv_shows.index("black mirror"))


# TUPLAS (inmutables)
months = ("Enero", "Febrero", "Marzo", "Abril")
print(len(months))
