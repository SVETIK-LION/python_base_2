"""
Задайте список из нескольких чисел.
Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""


def sum_odd_index_numbers(lst: list):
    odd_index_numbers = [lst[i] for i in range(len(lst)) if i % 2 != 0]
    sum_odd = sum(odd_index_numbers)

    return sum_odd


numbers = [2, 3, 5, 9, 3]
print(sum_odd_index_numbers(numbers))
