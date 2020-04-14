""" В диапазоне натуральных чисел от 2 до 99 определить,
    сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

j = 2
j_count = [0 for _ in range(10)]

for i in range(2, 100):
    for j in range(2, 10):
        if not i % j:
            j_count[j] += 1

for i in range(2, 10):
    print(f'для числа {i} ответ {j_count[i]}')
