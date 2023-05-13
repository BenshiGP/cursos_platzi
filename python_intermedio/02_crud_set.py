set_countries = {'mex', 'col', 'bol'}

size = len(set_countries)
print(size)

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
