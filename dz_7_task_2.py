""" Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
    заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и
    отсортированный массивы.
"""
# НЕ СДЕЛАЛ.. голова не варит, постоянно отвлекают; лучше оставлю как есть иначе поубиваю всех вокруг..

import random


# def merge_sort(arr, first, last):
#     if last <= first:
#         return arr
#     elif len(arr) == 2:
#         if arr[0] > arr[1]:
#             arr[0], arr[1] = arr[1], arr[0]
#
#     middle = (last - first) // 2 + first
#     first_half = merge_sort(arr, first, middle - 1)
#     second_half = merge_sort(arr, middle, last)


array = []
i = 1
while i <= 10:
    a = random.uniform(0, 50)
    if a != 50:  # наверное есть какой-то более изящный способ, но я ничего лучше не придумал(
        array.append(a)
        i += 1
print(array)


# print(merge_sort(array, first=0, last=len(array) - 1))





