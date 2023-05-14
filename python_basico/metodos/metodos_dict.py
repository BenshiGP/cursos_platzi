diccionario = {
    "nombre": 'benjamin',
    "apellido": 'garcia',
    "edad": 18
}

# nos devuelve un objeto dict_item
claves = diccionario.keys()

# obteniendo un elemento con get() (si no encuentra nada el programa continua)
valor_de_kasdks = diccionario.get("kasdks")
print("hola papa, el programa continua")

# eliminando todo del diccionario
# diccionario.clear()

# eliminando un elemento del diccionario
diccionario.pop("nombre")

# obteniendo un elemento dict_items iterable
diccionario_iterbale = diccionario.items()

print(diccionario_iterbale)
