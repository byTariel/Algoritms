import random


array = [i for i in range(11)]
random.shuffle(array)
print(array)
# array = [8, 9, 4, 1, 0, 3, 7, 6, 2, 5]


n = 1
while n < len(array):
    change = 0
    for i in range(len(array) - n):  # ломал голову, как же сокращать при каждом пробеге на один последний элемент,
        # так как он уже отсортирован и неожиданно пришло озарение!) / назову это улучшение - I
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            change += 1
    if not change:  # если при последнем пробеге не было сделано перестановок, то выход / назову это улучшение - II
        break
    n += 1
    print(array)

print(array)  # специально не убираю, хоть это и дублирует последний вывод, так как по факту это дополнительное
# пробегание по массиву происходит, перед тем когда срабатывает break и так можно делать эспирическое отслеживание
# количества произведенных пробежек

# Итак, метод пробегает n элементов (кол-во столбцов) n раз (кол-во строк). Улучшение I влияет на столбцы,
# а улучшение II на строки. Получается, что улучшение I сокращает каждый раз кол-во столбцов на один и это делает
# из них n/2 (отсекает у матрицы (квадрата) нижний правый треугольник, а следовательно его площадь становится n**2/2).
# Улучшение II, при самых худших вариантах, дает экономию строк в 20% (я очень много раз делал рандом и считал;
# наверное есть какой-то математический метод, но я его не знаю). Таким образом, вторую n (кол-во строк) мы можем
# умножить на 0,8. Получаем 2n**2 / 5.
