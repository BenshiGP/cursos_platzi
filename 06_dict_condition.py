import random
countries = ["col", "mex", "bol", "pe"]
popultaion_v2 = {country: random.randint(1, 100) for country in countries}
print(popultaion_v2)

result = {country: population for (country, population) in popultaion_v2.items() if population > 50}

print(result)


text = "Hola, soy Benjamin"
unique = {c: c.upper() for c in text if c in "aeiou"}
print(unique)
