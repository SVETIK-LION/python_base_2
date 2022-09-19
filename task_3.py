"""
Задайте список из вещественных чисел.
Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

[1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""


def diff_max_min_fract(lst: list):
    fraction_parts = [num - int(num) for num in lst]

    return max(fraction_parts) - min(fraction_parts)


numbers = [1.1, 1.2, 3.1, 5, 10.01]
print(diff_max_min_fract(numbers))
