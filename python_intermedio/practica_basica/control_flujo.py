# 1- Escribir un programa que lea un número entero y determine si es par o impar.
"""
numero = int(input("Escribe un numero entero: --> "))
if numero % 2 == 0:
    print("el numero es par")
else:
    print("es impar")
""" 

# 2- Escribir un programa que solicite al usuario una lista de números y calcule 
# la suma de todos los números pares en la lista.
"""
numeros = input("Escriba un listado de numeros separados por , : --> ").split(",")
suma = 0 #variable inicializada en 0 para almacenar la suma de los numeros pares de la lista

for numero in numeros: #bucle for para iterar cada elemento de la lista
    if int(numero) % 2 == 0: #pasando los elementos de la lista a entero(int)
        suma += int(numero) #si el numero es par se agraga a la variable suma(suma = suma + numero par)

print(f"La suma de los numeros pares en la lista es {suma}")
"""

# 3- Escribir un programa que solicite al usuario una cadena de texto y cuente la cantidad de vocales que contiene.
"""
cadena = input("Escriba una frase: --> ")
suma_vocales = 0

for c in cadena:
    if c.lower() in "aeiou":
        suma_vocales += 1

print(f"la suma de las vocales es: {suma_vocales}")
"""

# 4- Escribir un programa que imprima la tabla de multiplicar de un número entero ingresado por el usuario.
numero = int(input("Ingrese un número entero: "))
"""

for i in range(1, 11):
    print(numero, "x", i, "=", numero*i)
"""

# 5- Calcular la suma de los primeros N números naturales
#Escribe un programa que solicite al usuario un número entero positivo N
# y calcule la suma de los primeros N números naturales.

"""
numero = int(input("Escribe un numero entero: "))
suma =  0
for i in range(1, numero+1):
    suma += i
    print(suma)
"""

# 6- Verificar si un número es primo
#Escribe un programa que solicite al usuario un número entero positivo y
# verifique si es un número primo.
#Un número es primo si es divisible únicamente por 1 y por sí mismo.

"""
numero = int(input("Escribe un numero entero: "))
def es_primo(num):
    if num > 1:
        for n in range(2, num):
            if num % n == 0:
                print("no es primo", n , "es divisor")
                return False
        print("es primo")
        return True    
    else:
        print("el numero debe ser mayor a 1")
        
print(es_primo(numero))
"""

# otra forma de saber si es primo o no
"""
if numero > 1:
    cont = 0
    i = 2
    for i in range(2,numero):
        resto = numero%i
        if resto == 0:
            cont += 1
    if cont == 0:
        print(f"el numero {numero} es primo ")
    else:
        print(f"el numero {numero} no es primo")
"""

# otra forma mas eficiente y rapida 
"""
if numero > 1:
    cont = 0
    i = 2
    while i<numero and cont==0:
        resto = numero%i
        if resto == 0:
            cont += 1
        i+=1
    if cont == 0:
        print(f"el numero {numero} es primo ")
    else:
        print(f"el numero {numero} no es primo")
"""      

# y si quiero mostrar los numeros primos de 1 hasta algun numero 
"""

for num in range(1, numero):
    if numero > 1:
        cont = 0
        i = 2
        while i < num and cont==0:
            resto = num % i
            if resto == 0:
                cont += 1
            i+=1
        if cont == 0:
            print(num)
            
"""

# 7- Imprimir los números impares entre 1 y N
# Escribe un programa que solicite al usuario un 
# número entero positivo N y muestre por pantalla todos los números impares entre 1 y N.

for num in range(1, numero+1):
    while numero > 1:
       if numero % num == 1:
            print(num)