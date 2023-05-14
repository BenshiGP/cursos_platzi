# creando una lista con list()
lista = list([34, 53, 23, True])


# Devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

# agregando un elemento a la lista
lista.append(645)

# agregando un elemento a la lista en un indeice especifico
lista.insert(2, "TOMA MAMA")

# agregando varios elementos a la lista
lista.extend([False, 2030])

# eliminando un elemento de la lista (por su indice)
# -1 para eliminar el unltimo, -2 para eliminar el anteultimo, y asi sucesivamente
lista.pop(3)

# removiendo un elemento por su valor
lista.remove("TOMA MAMA")

# eliminando todos los elementos de la lista
# lista.clear()

# ordenando la lista (si usamos el parametro reverse=true lo ordena en reversa) no usa streings
lista.sort()

# invirtiendo los elementos de una lista
lista.reverse()

# verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(53)

print(elemento_encontrado)


"""
Lista = [1, 2, 3, 4, 5]

Puede ser modificada
Cada elemento esta separado por una coma
Puede contener todo tipo de datos
Metodos para listas
Lista.metodo(indice,elemento) o

Lista.metodo(elemento)

Metodos importantes
.count(elemento) cuenta cuantas veces un elemento esta en una lista

.extend(lista) permite extender una lista agregándole los elementos de otra lista

.pop() elimina y retorna el ultimo elemento de la lista

.reverse() reversa el orden de la lista

.sort() ordena la lista de manera ascendente o descendente

Actualizar un valor

Lista = [1, 2, 3, 4, 5]

Lista[0] = -8

Lista = [-8, 2, 3, 4, 5], resultado de la lista luego de actualizar el valor

Agregar un elemento

Lista.append(indice,elemento) o

Lista.append(elemento) en este caso el nuevo elemento se agrega al final de la lista

Eliminar un elemento

Lista.remove(indice, elemento)

Métodos de las listas

append(): Añade un ítem al final de la lista.
clear(): Vacía todos los ítems de una lista.
extend(): Une una lista a otra.
count(): Cuenta el número de veces que aparece un ítem.
index(): Devuelve el índice en el que aparece un ítem (error si no aparece).
insert(): Agrega un ítem a la lista en un índice específico.
pop(): Extrae un ítem de la lista y lo borra.
remove(): Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos.
reverse(): Le da la vuelta a la lista actual.
sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor.
"""
