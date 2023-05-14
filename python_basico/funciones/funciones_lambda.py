numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# creando una funcion lambda para multiplicar por dos
# return automaticamente


def multiplicar_por_dos(x): return x*2

# creando una funcion que diga si es para es no, para que sea inpar es num % 2 == 1

# def es_par(num):
#    if (num % 2 == 0):
#        return True


# usando filter con una funcion comun
# numeros_pares = filter(es_par, numeros)


# creando lo mismo que antes pero con lambda
numeros_pares = filter(lambda numero: numero % 2 == 0, numeros)
print(list(numeros_pares))
