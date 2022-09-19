"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:

6782 -> 23
0,56 -> 11
"""


def sum_digits(number):
    """
    Считает сумму цифр числа
    :param number:
    :return:
    """
    try:
        sum_num = 0
        str_num = str(number)
        for i in str_num:
            if i.isdigit():
                sum_num += int(i)
            elif i == '.':
                continue
            else:
                raise TypeError

        return sum_num
    except TypeError:
        return f'Неверное значение. Нужно ввести вещественное число'


print(sum_digits(0.56))
