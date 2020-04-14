""" Определить, какое число в массиве встречается чаще всего.
"""


import random


size = 100
min_item = 0
max_item = 100
array = [random.randint(min_item, max_item) for i in range(size)]
print(array)  # проверка

for i in range(len(array)):  # отстой((, на миллионе не завис, но результата я не дождался
    for j in range(i, len(array)):
        if array[i] > array[j]:
            array[i], array[j] = array[j], array[i]
print(array)  # проверка

count = 1
max_count = 1
number = 'никакое число не встречается больше'
for i in range(len(array) - 1):
    if array[i] == array[i + 1]:
        count += 1
        if count > max_count:
            max_count = count
            number = array[i]
    else:
        count = 1

print(f'число {number} встречается {max_count} раза' if max_count > 1 else f'{number} {max_count} раза')




