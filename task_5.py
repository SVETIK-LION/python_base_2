"""
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""


def fibo_list(number: int):
    fibo_nums = []

    a, b = 1, 1
    for _ in range(number):
        fibo_nums.append(a)
        a, b = b, a + b

    a, b = 0, 1
    for _ in range(number + 1):
        fibo_nums.insert(0, a)
        a, b = b, a - b

    return fibo_nums


print(fibo_list(8))
