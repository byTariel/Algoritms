""" В массиве случайных целых чисел поменять местами минимальный
    и максимальный элементы.
"""

import random


size = 1_000_000
min_item = 0
max_item = 100
array = [random.randint(min_item, max_item) for i in range(size)]

j = -1
max_number = min_number = array[0]
id_max, id_min = 0, 0
for i in array:
    j += 1
    if i > max_number:
        max_number = i
        id_max = j
    elif i < min_number:
        min_number = i
        id_min = j

print(array)
print(id_max, max_number)
print(id_min, min_number)

array[id_min], array[id_max] = array[id_max], array[id_min]

print(array)

