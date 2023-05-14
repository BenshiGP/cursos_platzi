# creando diccionarios con dict()
diccionario = dict(nombre="benjamin", apellido="garcia")

# las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["dalto", "rancio"]): "jajas"}

# creando diccionarios con fromkeys() valor por defecto none
diccionario = dict.fromkeys(["nombre", "apellido"])

# creando diccionarios con fromkeys() cambiando valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre", "apellido"], "no se")

print(diccionario)

# NO PODES HACER DICCIONARIOS VACIOs A NO SER QUE USEMOS LA FUNCION dict()
