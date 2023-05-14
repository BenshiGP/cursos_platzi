"""

Principio DRY
Las funciones nos ayudan a cumplir con uno de los principios más importantes
de la programación como lo es el principio DRY (don’t repeat yourself) o (no te repitas).

Al tener la lógica en una función evitas tener que escribir la misma lógica una
y otra vez, de modo que tienes un código más limpio y más escalable.

"""
"""
def my_function(parametros):
    pass
    
#invocar funcion
my_function(arguments)
"""

def my_print(text):
    print(text * 2)

my_print("como va la gente")

a = 10
b = 90

c = a + b

def suma(a, b):
    my_print(a + b)

suma(20, 43)
suma(20, 13)