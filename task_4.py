"""
Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
многочлена и записать в файл многочлен степени k.

Пример:

k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""


from random import randint


def polynomial(coefficients: list):
    poly = ''
    for i in range(len(coefficients)):
        poly += f'{coefficients[i]}'
        if i != 0:
            poly += f'x^{i}'
        if i != len(coefficients) - 1:
            poly += f' + '

    return f'{poly} = {0}'


coeff = [randint(0, 100) for i in range(10)]
print(polynomial(coeff))

with open('poly.txt', 'w') as f:
    f.write(polynomial(coeff))
