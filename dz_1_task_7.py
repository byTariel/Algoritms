""" По длинам трех отрезков, введенных пользователем,
    определить возможность существования треугольника,
    составленного из этих отрезков. Если такой треугольник существует,
    то определить, является ли он разносторонним,
    равнобедренным или равносторонним.
"""


a, b, c = map(int, input('введите длины трех отрезков через пробел: ').split())
if a + b > c:
    if a + c > b:
        if b + c > a:
            if a == b == c:
                print('треугольник равносторонний')
            elif a != b and b != c and a != c:
                print('треугольник разносторонний')
            else:
                print('треугольник равнобедренный')
else:
    print('такого треугольника не существует')
