items = [
    {
        "product" : "camisa",
        "price" : 100,
    },
    {
        "product" : "pantalones",
        "price" : 300
    },
    {
        "product" : "pantalones 2",
        "price" : 200
    }
]

def add_taxes(item):
    new_item = item.copy()
    new_item["taxes"] = new_item["price"] * .19
    return new_item

new_items = list(map(add_taxes, items))
print("new list")
print(new_items)
print("old list")
print(items)


print("---------------")
print("---------------")
print("---------------")
print("---------------")


empleados = [
    {
        "empleado" : "juan",
        "salario" : 1200 
    },
    {
        "empleado" : "marcos",
        "salario" : 1500
    }
]
print(empleados)
def increase_salario(price):
    price["salario"] = price["salario"] * 1.20 
    return price
    
    
nuevo_salario = list(map(increase_salario, empleados))
print(f"su nuevo salario es {nuevo_salario}")

print("---------------")
print("---------------")
print("---------------")
print("---------------")

productos = {'Leche': 85, 'Queso': 120, 'Huevos': 70, 'Pan': 60, 'Jamón': 150}
precios_actualizados = list(map(lambda x: (x[0], x[1] * .8) if x[1] > 100 else (x[0], x[1]), productos.items()))
print(precios_actualizados)


print("---------------")
print("---------------")
print("---------------")
print("---------------")


personas = {'Juan': 30, 'María': 25, 'Pedro': 40}
datos_actualizados = list(map(lambda x: (x[0].upper(), x[1] * 2), personas.items()))
print(datos_actualizados)

print("---------------")
print("---------------")
print("---------------")
print("---------------")

population = {
    "Argentina" : 1000,
    "chile" : 670,
    "paraguay": 350
}

population_update = list(map(lambda x: (x[0], x[1] * 1.05), population.items()))
print(population_update)

print("---------------")
print("---------------")
print("---------------")
print("---------------")

productos = [
    {
        "product" : "leche",
        "price" : 100,
        "inventory" : 15
    },
    {
        "product" : "jamon",
        "price" : 500,
        "inventory" : 8
    },
    {
        "product" : "pan",
        "price" : 400,
        "inventory" : 29
    },
    {
        "product" : "azucar",
        "price" : 200,
        "inventory" : 4
    }    
]
     
def descuentos(x):
    if x["inventory"] < 10:
        x["price"] *= .9
    else:
        x["price"] = x["price"]
    return x    

result = list(map(descuentos, productos))
print(result)    

print("otra forma de resolver el ejercico de arriba")

productos = [
    {
        "product" : "leche",
        "price" : 100,
        "inventory" : 15
    },
    {
        "product" : "jamon",
        "price" : 500,
        "inventory" : 8
    },
    {
        "product" : "pan",
        "price" : 400,
        "inventory" : 29
    },
    {
        "product" : "azucar",
        "price" : 200,
        "inventory" : 4
    }    
]

result = list(map(lambda x: {"product": x["product"], "price": x["price"]*0.9 if x["inventory"] < 10 else x["price"], "inventory": x["inventory"]}, productos))

print(result)
