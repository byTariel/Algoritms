from collections import defaultdict, Counter


balance_sheet = defaultdict(list)
company_number = int(input('введите кол-во предприятий: '))
for i in range(company_number):
    name = input(f'введите название предприятия {i + 1}: ')
    for j in range(2):
        balance_sheet[name].append(int(input(f'введите прибыль за {j + 1} квартал: ')))
print(balance_sheet)  # для проверки и наглядности

dict_sum_total = Counter()
sum_total = 0  # by all company
for el in balance_sheet:
    s = 0
    for n in balance_sheet[el]:  # sum(balance_sheet[el])
        s += n
    sum_total += s
    dict_sum_total[el] = s


for i in dict_sum_total:  # при упорядоченном не понадобилось дважды пробегать словарь,
    # чтобы сначала вывести только тех, которые больше
    if dict_sum_total[i] > sum_total/company_number:
        print(f'прыбыль выше среднего: {i}')
    elif dict_sum_total[i] < sum_total/company_number:
        print(f'прыбыль ниже среднего: {i}')
