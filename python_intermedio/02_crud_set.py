set_countries = {'mex', 'col', 'bol'}

size = len(set_countries)
print(size)

# retorna booleanos 
print("col" in set_countries)
print("pe" in set_countries)

# add
set_countries.add("pe")
print(set_countries)

# update
set_countries.update({"arg", "ecua"})
print(set_countries)

# remove
set_countries.remove("pe")
print(set_countries)

# set_countries.remove("usa")
set_countries.discard("usa")
print(set_countries)

# limpiar la lista completa
set_countries.clear()
print(set_countries)

"""
Funciones de set:

add(): Añade un elemento.

update(): Añade cualquier tipo de objeto iterable como: listas, tuplas.

discard(): Elimina un elemento y si ya existe no lanza ningún error.

remove(): Elimina un elemento y si este no existe lanza el error “keyError”.

pop(): Nos devuelve un elemento aleatorio y lo elimina y si el conjunto está vacío lanza el error “key error”.

clear(): Elimina todo el contenido del conjunto.
"""