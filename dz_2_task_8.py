""" Посчитать, сколько раз встречается определенная цифра в введенной
    последовательности чисел. Количество вводимых чисел и цифра,
    которую необходимо посчитать, задаются вводом с клавиатуры.
"""


n = int(input('введите количество чисел для ввода: '))
a = input('введите цифру для поиска: ')
entered_numbers, mention_digit = 0, 0
while entered_numbers < n:
    number = input(f'введите {entered_numbers + 1} натуральное число: ')
    for i in number:
        if i == a:
            mention_digit += 1
    entered_numbers += 1

print(f'в введенной последовательности чисел цифра {int(a)} '
      f'встретилась {mention_digit} '
      f'раз{"а" if mention_digit % 10 == 2 or mention_digit % 10 == 3 or mention_digit % 10 == 4 else ""}')
      # f'раз{"а" if mention_digit in [2, 3, 4] else ""}')
