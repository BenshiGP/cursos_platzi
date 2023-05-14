"""

Dentro de una función puede haber variables, las cuales se llaman variables locales.
Estas variables locales, se identifican porque están escritas dentro de la definición de la función;
y únicamente funcionan mientras que la función sea llamada o utilizada. Si vas a llamar a una variable
local por fuera de la función, no servirá.
Y existen variables globales, que son las que están escritas fuera de una función.
Estas variables si funcionan al ser llamadas sin la función, porque no están determinadas dentro de la función.

"""

price = 100  # global en este archivo


def increment():
    price = 1000  # solo se puede usar en la funcion, local scope
    result = price + 10
    print(result)
    return result


print(price)
price_2 = increment()
print(price_2)
