# https://drive.google.com/file/d/1Ih5bKxGSuZ8i-fibtftnasH5_IM6l-GY/view?usp=sharing
""" Найти сумму и произведение цифр трехзначного числа,
    которое вводит пользователь.
"""


n = int(input('введите трехзначное число: '))
a = n // 100
b = n % 100 // 10
c = n % 10
sum_numbers = a + b + c
multiply_numbers = a * b * c

print(f'сумма цифр числа {n} равна {sum_numbers}, '
      f'а произведение равно {multiply_numbers}')
