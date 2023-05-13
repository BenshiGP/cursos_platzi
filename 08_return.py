def suma_range(min, max):
    sum = 0
    for x in range(min, max):
        sum += x
    return sum


result = suma_range(1, 10)
print(result)
result_1 = suma_range(result, result + 2)
print(result_1)
