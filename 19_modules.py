import sys 
print(sys.path) #sirve para ver la ruta de donde se ejecuta el archivo .py

import re
text = "Mi numero de telefono es 311 123 121, el codigo del pais es 57, mi numero de la suerte es el 7"
result = re.findall("[0-9]+", text)
print(result)

import time 
timestamp = time.time()
local = time.localtime()
result = time.asctime(local)
print(result)

import collections
numbers = [1,1,1,2,2,2,2,1,1,3,3,3,3,4,4,4,4,5,5,12]
counter = collections.Counter(numbers)
print(counter)