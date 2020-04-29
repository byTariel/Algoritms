""" Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
    заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный
    и отсортированный массивы.
"""
import random, math


def bubble_sort(array):
    n = 1
    while n < len(array):
        change = 0
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:  # чуть не забыл, блин..!
                array[i], array[i + 1] = array[i + 1], array[i]
                change += 1
        if not change:
            break
        n += 1


package = [math.floor(random.uniform(-1, 1) * 100) for i in range(11)]
print(package)
print('*' * 100)
bubble_sort(package)
print(package)
