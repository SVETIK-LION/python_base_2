"""
Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
"""


from random import randint


with open('file.txt', 'w') as f:
    f.write('1\n3\n4\n10')

with open('file.txt', 'r') as f:
    positions = [int(line.strip()) for line in f]


def random_list(n: int):
    lst = [randint(-n, n) for _ in range(n)]
    return lst


def mult_digits(numbers_list: list, positions_list: list):
    mult = 1
    for i in positions_list:
        mult *= numbers_list[i - 1]
    return mult


print(random_list(10))
print(mult_digits(random_list(10), positions))
