""" Пользователь вводит две буквы.
    Определить, на каких местах алфавита они стоят,
    и сколько между ними находится букв.
"""


a = input('введите первую букву: ')
b = input('введите вторую букву: ')

a_number = ord(a) - 96
b_number = ord(b) - 96
if a_number != b_number:
    n = abs(a_number - b_number) - 1
else:
    n = 0

print(f'номер в алфавите первой буквы "{a}" = {a_number};'
      f' второй буквы "{b}" = {b_number};'
      f' а букв между ними = {n}')
