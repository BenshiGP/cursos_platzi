price = 100  # global en este archivo


def increment():
    price = 1000  # solo se puede usar en la funcion
    result = price + 10
    print(result)
    return result


print(price)
price_2 = increment()
print(price_2)
