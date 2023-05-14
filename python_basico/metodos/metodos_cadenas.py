cadena1 = "Hola,maquina,soy,benja"
cadena2 = "Bienvenido raai"

# convierte a mayusculas
mayusc = cadena1.upper()

# convierte a minuscula
minusc = cadena1.lower()

# primera letra en mayuscula
primer_letra_mayusc = cadena1.capitalize()

# buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1
busqueda_find = cadena1.find("B")

# buscamos una cadena en otra cadena, si no hay coincidencias lanza una excepcion
busqueda_index = cadena1.index("a")

# si es numerico, devolvemos true, sino devolvemos false
es_numerico = cadena1.isnumeric()

# si es alfanumerico devolvemos true, sino devolvemos false
es_alfanumerico = cadena1.isalpha()

# contamos las coincidencias de una cadena dentro de otra cadena, devuelve la cantidad
# de coincidencias
contar_coincidencias = cadena1.count("a")

# contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

# verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true
empieza_con = cadena1.startswith("Ho")

# verificamos si una cadena termina con otra cadena dada, si es asi devuelve true
termina_con = cadena1.endswith("benja")

# remplaza un pedazo de la cadena dada, por otra dada
cadena_nueva = cadena1.replace("Hola", "Hola genio idolo")

# separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")


print(cadena_separada)
