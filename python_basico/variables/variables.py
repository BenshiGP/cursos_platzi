# LAS VARIABLES SON ESPACIOS QUE SE ALMACENAN EN LA MEMORIA DE NUESTRO PROGRAMA LAS CUALES
# SE PUEDEN REUTILIZAR

# Definiendo una variable con camelCase
nombreCompletoDeTuTioMaster = 'benshi gp'

# Definiendo una variable con snake_case
nombre_completo_de_tu_tio_master = 'benshi gp'

a = 5
b = 9

c = a + b

print(c)

numero = 10
numero += 1
numero -= 9

print(numero)

# concatenar con +
nombre = 'Benja'
bienvenida = 'Hola ' + nombre + ' ¿Como estas?'

print(bienvenida)


# EL f-STRING SIRVE PARA PASAR CUALQUIER VALOR A UNA CADENA DE TEXTO YA SEAN NUMEROS O BOOLEANOS
nombre = 45
bienvenida = f'Hola {nombre} ¿Como estas?'

print(bienvenida)
# OPERADORES DE PERTENENCIA (IN / NOT IN)
print('hola' not in bienvenida)  # true
print('hola' in bienvenida)  # false
