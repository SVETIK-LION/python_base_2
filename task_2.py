"""
Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

[2, 3, 4, 5, 6] => [12, 15, 16];
[2, 3, 5, 6] => [12, 15]
"""


from math import ceil


def mult_pairs_numbers(lst: list):
    mult_lst = [lst[i] * lst[-i - 1] for i in range(ceil(len(lst) / 2))]

    return mult_lst


my_lst_1 = [2, 3, 4, 5, 6]
my_lst_2 = [2, 3, 5, 6]

print(mult_pairs_numbers(my_lst_1))
print(mult_pairs_numbers(my_lst_2))
