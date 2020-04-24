""" Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
    Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
    в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы
"""
# на уроке сказал, что могу в одну строчку решить, но это было ошибкой; понял это когда стал решать.
# Было ошибочное предположение, что это среднее арифметическое округленное до целого вниз,
# но это всего лишь частный случай при удачных цифрах. Ниже полноценное решение:
import random


m = 2
array = [random.randint(0, 10) for i in range(2 * m + 1)]
print(array)

while len(array) > 1:
    min_ = max_ = array[0]
    for i in range(len(array) - 1):
        if array[i + 1] > max_:
            max_ = array[i + 1]
        elif array[i + 1] < min_:
            min_ = array[i + 1]
    array.remove(min_)
    array.remove(max_)

print(array)
