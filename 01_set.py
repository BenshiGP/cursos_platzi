"""
Sets
Se pueden modificar
No tienen un orden
No pueden tener elementos duplicados

"""

set_countries = {'mex', 'col', 'bol'}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 2, 443, 32}
print(set_numbers)

set_types = {1, "hola", False, 23, 4.3}
print(set_types)

set_from_string = set("hoola")
print(set_from_string)

set_from_tuples = set(("abc", "cbv", "as", "abc"))
print(set_from_tuples)

numbers = [1, 2, 3, 1, 2, 3, 5, 4]
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)


# no tiene un par key-value, así me doy cuenta que es un set, un conjunto.
set_countries = {'col', 'mex', 'bol'}
print(set_countries)

# si yo pongo algo repetido, él me lo quita al imprimir
set_countries2 = {'col', 'mex', 'bol', 'col'}
print(set_countries2)  # {'col', 'mex', 'bol'}

# puede ser mixto. El set se ordena solo, lo importante es lo que tengo dentro.
set_types = {1, 'hola', False, 12.12}
print(set_types)  # {False, 1, 12.12, 'hola'}

# la podemos crear a partir de un string
set_from_string = set('hoola')
print(set_from_string)  # {'a', 'l', 'o', 'h'}

# la podemos crear a partir de una tupla
set_from_tuples = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuples)  # {'as', 'abc', 'cbv'}

# la podemos crear a partir de una lista
numbers = [1, 2, 3, 1, 2, 3, 4]
set_numbers = set(numbers)
print(set_numbers)  # {1, 2, 3, 4}
# si quiero convertir este set único a una lista, lo puedo hacer:
unique_numbers = list(set_numbers)
print(unique_numbers)
