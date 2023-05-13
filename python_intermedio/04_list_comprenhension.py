# element    for element in iterable
# elemento - ciclo donde se extraeb ekenebtos de cualquier iterable

"""
numbers = []
for i in range(1, 11):
    numbers.append(i * 2)
print(numbers)


numbers_v2 = [i * 2 for i in range(1, 11)]
print(numbers_v2)
"""

numbers = []
for i in range(1, 11):
    if i % 2 == 0:
        numbers.append(i * 2)
print(numbers)

numbers_v2 = [i * 2 for i in range(1, 11) if i % 2 == 0]
print(numbers_v2)


# Crea una lista que contenga los primeros 10 números pares (empezando desde el número 2).
pares = [n for n in range(2, 22) if n % 2 == 0]
print(pares)
# Crea una lista que contenga los primeros 15 múltiplos de 3 (empezando desde el número 3).
multi = [n*3 for n in range(3, 16)]
print(multi)
# Dada una lista de números [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
# crea una nueva lista que contenga solo los números pares de la lista original.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares_2 = [i for i in nums if i % 2 == 0]
print(pares_2)

# Crea una lista que contenga los cuadrados de los números impares del 1 al 10.
cuadrados_impares = [n**2 for n in range(1, 11) if n % 2 != 0]
print(cuadrados_impares)

# Dada una lista de palabras ['hola', 'mundo', 'python', 'es', 'genial'],
# crea una nueva lista que contenga solo las palabras que tienen más de 4 letras.

palabras = ['hola', 'mundo', 'python', 'es', 'genial']
letras_4 = [i for i in palabras if len(i) > 4]
print(letras_4)
