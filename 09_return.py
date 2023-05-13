def find_volume(lenght=3, width=4, depth=5):
    return lenght * width * depth, "hola", lenght


# desempaquetnado la tupla realizadaen el  return
result, text, lenght = find_volume(depth=2)
print(result)
print(text)
print(lenght)
