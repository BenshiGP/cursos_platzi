# key:value                for var in iterable
# elemento llave-valor -   ciclo donde se extraen elementos de cualquier iterable

"""
dict = {}
for i in range(1, 5):
    dict[i] = i * 2

print(dict)

dict_v2 = {i: i * 2 for i in range(1, 5)}
print(dict_v2)
"""

"""
import random
countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
    population[country] = random.randint(1, 100)

print(population)


popultaion_v2 = {country: random.randint(1, 100) for country in countries}
print(popultaion_v2)
"""

"""
La funcion zip() hace una union entre una lista y otra,
creando una lista con tuplas,
[('benja', 12), ('mati', 23), ('santi', 54)]
"""
names = ["benja", "mati", "santi"]
ages = [12, 23, 54]

print(list(zip(names, ages)))

new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)

# Crear un diccionario con los cuadrados de los primeros 5 números enteros:
cuadrados = {n: n**2 for n in range(1, 6)}
print(cuadrados)

# Crear un diccionario a partir de dos listas, una con claves y otra con valores:
# utilizando la funcion zip() para combinar dos listas en una lista de tuplas
autos = ["falcon", "ferrari", "gol", "suran"]
precios = [1000000, 2700000, 1500000, 2000000]
concecionario = {car: price for (car, price) in zip(autos, precios)}
print(concecionario)

# Crear un diccionario a partir de una lista de tuplas:
tupla = [("benja", 18), ("santi", 20), ("bauti", 19)]
diccionario = {name: age for (name, age) in tupla}
print(diccionario)

# Crear un diccionario con los caracteres de una cadena
# como claves y el número de veces que aparecen como valores:
cadena = "Hola mundo Python ta piola"
cadena_dict = {chars: cadena.count(chars) for chars in cadena}
print(cadena_dict)
