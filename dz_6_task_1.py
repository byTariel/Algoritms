""" Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
    программах в рамках первых трех уроков. Проанализировать результат и определить
    программы с наиболее эффективным использованием памяти."""

""" 4.1. Сформировать из введенного числа обратное по порядку входящих в него цифр
    и вывести на экран. Например, если введено число 3486, надо вывести 6843.
    dz_2_task_3.
"""
# решил выбрать именно эту задачу, так как тут на анализ быстродействия потратил больше всего времени
# и стало интересно сравнить их теперь по ресурсо затратам; расчет по каждому из четырех решений в конце.


import timeit
import cProfile
import sys
sys.setrecursionlimit(3010)


# первый вариант: (линейная зависмость). Удвоение Х дает увеличение У примерно тоже в 2 раза за шаг.
def func_while(n, reverse_n):
    while n > 0:
        reverse_n += str(n % 10)
        n //= 10
    return int(reverse_n)
# cProfile.run('func_while(1_000**1_000, "")')  # 1    0.018    0.018    0.018    0.018 dz_4_task_1.py:12(func_while)


# второй вариант: (линейная зависмость) !!! самое быстрое !!! Удвоение Х дает увеличение У примерно в 1.5 раз за шаг.
def func_for(n, reverse_n):
    n = str(n)
    for i in n:
        reverse_n = i + reverse_n
    return int(reverse_n)
# cProfile.run('func_for(1_000**1_000, "")')  # 1    0.002    0.002    0.002    0.002 dz_4_task_1.py:31(func_for)
# # САМЫЙ БЫСТРЫЙ СПОСОБ


# третий вариант: рекурсия остатков от деления (линейная зависмость).
# Удвоение Х дает увеличение У примерно в 1.8 раз за шаг.
def func_cut(n, reverse_n):
    if n <= 0:
        return int(reverse_n)
    return func_cut(n // 10, reverse_n + str(n % 10))
# cProfile.run('func_cut(1_000**1_000, "")')  # 3002/1    0.026    0.000    0.026    0.026 dz_4_task_1.py:63(func_cut)


# четвертый вариант: рекурсия срезов (линейная зависмость). Удвоение Х дает увеличение У примерно в 1.8 раз за шаг.
def func_slice(n, reverse_n):
    n = str(n)
    if n == '':
        return int(reverse_n)
    return func_slice(n[1:], n[0] + reverse_n)
# cProfile.run('func_slice(1_000**1_000, "")')  # 3002/1   0.011   0.000   0.011   0.011 dz_4_task_1.py:83(func_slice)
# # эта рекурсия в два раза эффективнее предыдущей


def show(x):
    global sum_item
    sum_item += sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show(key)
                show(value)
        elif not isinstance(x, str):
            for item in x:
                show(item)
    return sum_item


n = 1000**1000
reverse_n = ""


z = (func_while, func_for, func_cut, func_slice)
for i in z:
    sum_item = 0
    sum_all = 0
    x = [n, reverse_n, i]
    for j in x:
        sum_all += show(x)
    print(f'объем занятой памяти при использовании функции {i} равен {sum_all}')


# 1 вариант: объем занятой памяти при использовании функции <function func_while at 0x0031E540> равен 8922
# 2 вариант: объем занятой памяти при использовании функции <function func_for at 0x00543810> равен 8922
# 3 вариант: объем занятой памяти при использовании функции <function func_cut at 0x00543858> равен 8922
# 4 вариант: объем занятой памяти при использовании функции <function func_slice at 0x005438A0> равен 8922




# # проверка
# def test_func(func):
#     checkup = 5001
#     assert checkup == func(100500, '')
#     print(f'тест ОК')
#
#
# # test_func(func_slice)
# # test_func(func_cut)
# # test_func(func_while)
# # test_func(func_for)
