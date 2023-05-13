"""

Normalmente solemos usar parámetros y argumentos como sinónimos, y en la 
práctica podemos inferir lo que esto significa según el contexto. Pero en 
un entorno profesional, deberíamos tener muy claro que los parámetro son 
las reglas o instrucciones que definimos dentro de la función, mientras los
argumentos son los datos que le pasamos a la función para que los “reemplace”
y ejecute la función.

Algo así como en matemáticas básicas, cuando definimos y = x^2 + x + 3, 
la derecha de la ecuación serían los parámetros, mientras que los argumentos, 
serían los valores que le asignamos a la x, bien sea para encontrar las coordenadas
de un punto (una iteración), o para trazar la gráfica completa (multiples iteraciones)…

**Parámetros: **Reglas Internas de la Función.

**Argumentos: **Datos Externos que le Pasamos a la Función para que Pueda Hacer sus Cálculos.

"""


def increment(x):
    return x + 2

increment_v2 = lambda x: x + 1

def high_ord_func(x, func):
    return x + func(x)

high_ord_func_v2 = lambda x,func: x+ func(x)
    
result = high_ord_func(5,increment)
print(result)    

result_v2 = high_ord_func_v2(2,increment)
print(result_v2)

result_v3 = high_ord_func_v2(2,lambda x: x * 3)
print(result_v3)
