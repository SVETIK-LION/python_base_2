"""
Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.
"""


# Открываем файлы, читаем многочлены и записываем их в переменные
with open('poly_1.txt', 'r') as f:
    poly_1 = f.read()

with open('poly_2.txt', 'r') as f:
    poly_2 = f.read()

# Превращаем в список членов
poly_list_1 = poly_1.split(' + ')
poly_list_2 = poly_2.split(' + ')

# Выделяем свободные члены в отдельный список и удаляем из основных
free_members = []

for el in poly_list_1:
    if 'x' not in el:
        free_members.append(int(el))
        poly_list_1.remove(el)

for el in poly_list_2:
    if 'x' not in el:
        free_members.append(int(el))
        poly_list_2.remove(el)

print(f'Список свободных членов: {free_members}')

# Сортируем списки членов по степени
poly_sort_1 = sorted(poly_list_1, key=lambda x: int(x[-1]))
poly_sort_2 = sorted(poly_list_2, key=lambda x: int(x[-1]))

print(f'Список отсортированных по степени членов 1: {poly_sort_1}')
print(f'Список отсортированных по степени членов 2: {poly_sort_2}')

# Отделяем коэффициенты
coeff_split_1 = list(map(lambda s: s.split('x'), poly_sort_1))
coeff_split_2 = list(map(lambda s: s.split('x'), poly_sort_2))

print(coeff_split_1)
print(coeff_split_2)

# Результат сложения свободных членов
free_members_res = sum(free_members)
print(f'Сумма свободных членов: {free_members_res}')

# Коэффициенты
coeff_1 = list(map(lambda x: int(x[0]), coeff_split_1))
coeff_2 = list(map(lambda x: int(x[0]), coeff_split_2))

print(f'Коэффициенты, кроме свободных 1: {coeff_1}')
print(f'Коэффициенты, кроме свободных 2: {coeff_2}')

# Сложение двух списков коэффициентов, кроме свободных
coeff_res = list(map(sum, zip(coeff_1, coeff_2)))
print(f'Результат сложения коэффициентов, кроме свободных: {coeff_res}')

# Список всех коэффициентов нового многочлена
coeff_res.insert(0, free_members_res)
print(f'Список всех коэффициентов нового многочлена: {coeff_res}')


def polynomial(coefficients: list):
    """
    Создает многочлен из списка коэффициентов\n
    :param coefficients:
    :return:
    """
    poly = ''
    for i in range(len(coefficients)):
        poly += f'{coefficients[i]}'
        if i != 0:
            poly += f'x^{i}'
        if i != len(coefficients) - 1:
            poly += f' + '

    return f'{poly} = {0}'


print(f'Результат сложения двух многочленов: {polynomial(coeff_res)}')
