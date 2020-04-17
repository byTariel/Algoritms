from collections import deque


def accumulation_sum(pos, remember):
    if pos + remember <= 15:
        final.appendleft(check[pos + remember])  # выгода от deque
        remember = 0
        return remember
    else:
        final.appendleft(check[pos + remember - 16])  # выгода от deque
        remember = 1
        return remember


check = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
first = deque(input('введите первое шестнадцатиричное число: ').upper())
second = deque(input('введите второе шестнадцатиричное число: ').upper())
final = deque()  # результат суммы двух чисел
if len(first) > len(second):
    first, second = second, first
remember = 0

while first:
    a = first.pop()
    b = second.pop()
    pos = check.index(a) + check.index(b)
    remember = accumulation_sum(pos, remember)

while second:
    if remember:
        c = second.pop()
        pos = check.index(c)
        remember = accumulation_sum(pos, remember)
    else:
        final.appendleft(second.pop())
else:
    if remember:
        final.appendleft('1')

print(f'сумма чисел равна {list(final)}')
