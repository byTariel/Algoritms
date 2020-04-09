""" Сформировать из введенного числа обратное по порядку входящих в него цифр
    и вывести на экран. Например, если введено число 3486, надо вывести 6843
"""


# первый вариант
n = int(input('введите любое натуральное число: '))
reverse_number = ''
while n > 0:
    reverse_number += str(n % 10)
    n //= 10

print(int(reverse_number))


# второй вариант
n = input('введите любое натуральное число: ')
reverse_n = ''
for i in n:
    reverse_n = i + reverse_n

print(int(reverse_n))


""" поппытка сравнить эффективность двух способов:
    сложность первого: 3 * len(n)
    сложность второго: (len(n) + 1) * len(n) / 2
    6 * len(n) / 2  ~  (len(n) + 1) * len(n) / 2
                 6  ~  len(n) + 1    
    получается, что если длина числа больше 5, то предпочтительнее первый вариант
"""


# первый вариант, рекурсия (блок-схема: task_3(2))
def func(n, reverse_number):
    if n <= 0:
        return int(reverse_number)
    return func(n // 10, reverse_number + str(n % 10))


n = int(input('введите любое натуральное число: '))
reverse_number = ''
print(func(n, reverse_number))


# второй вариант, рекурсия - пока не придумал


# # запрещенная рекурсия
# def func(n, reverse_n):
#     if n == '':
#         return int(reverse_n)
#     return func(n[1:], n[0] + reverse_n)
#
#
# n = input('введите любое натуральное число: ')
# reverse_n = ''
# print(func(n, reverse_n))
