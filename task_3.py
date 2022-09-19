"""
Задайте список из n чисел последовательности Sn = (Sn-1 + 3) и выведите на экран их сумму.
"""


def numbers_dict(n):
    num_dict = {
        1: 4
    }

    for i in range(2, n + 1):
        num_dict[i] = num_dict[i - 1] + 3

    return num_dict


print(numbers_dict(6))
