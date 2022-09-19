"""
Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

45 -> 101101
3 -> 11
2 -> 10
"""


def decimal_to_binary(number: int):
    bin_num = ''
    while number != 0:
        digit = number % 2
        bin_num += str(digit)
        number //= 2

    return bin_num


print(decimal_to_binary(45))
