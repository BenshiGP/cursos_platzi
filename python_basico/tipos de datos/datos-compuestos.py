# Son datos que adentro tiene otros datos simples o compuestos pero que se pueden agrupar

# LISTAS
lista = [" Tomas Benjamin ", "Garcia Ponce", True, 1.72]
# LA TUPLA ES LO MISMO QUE LA LISTA PERO ESTA NO SE PUEDE MODIFICAR
tupla = (" Tomas Benjamin ", "Garcia Ponce", True, 1.72)

# esto es valido
lista[3] = "maquinola"

# esto no es valido
# tupla[3] = "maquinola"

# Crando un conjunto (set) (no se accede a elementos por indice, no almacena datos duplicados)
conjunto = {" Tomas Benjamin ", "Garcia Ponce", True, 1.72}

# print(conjunto[3]) -> NO PUEDE ACCEDER AL ELEMENTO

# Creando un diccionario (dict) (la estructura es key : value y separamos con comas)
diccionario = {
    'nombre': "Tomas Benjamin",
    'apellido': "Garcia Ponce",
    'quiere_aprender': True,
    'altura': 1.73,
    'dato_duplicado': "Tomas Benjamin"
}
