"""
Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
"""


def mult_digits(number: int):
    """
    Принимает на вход число N и выдает набор произведений чисел от 1 до N\n
    :param number:
    :return:
    """
    result = []
    mult = 1
    for i in range(1, number + 1):
        mult *= i
        result.append(mult)

    return result


print(mult_digits(4))
