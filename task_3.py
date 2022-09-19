"""
Задайте последовательность чисел.
Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
"""


# Вариант 1
def uniq_elem(lst: list):
    new_lst = []
    [new_lst.append(i) for i in lst if i not in new_lst]

    return new_lst


my_list = [1, 3, 10, 10, 10, 4]

print(uniq_elem(my_list))


# Вариант 2
uniq_elem_2 = set(my_list)
print(uniq_elem_2)
