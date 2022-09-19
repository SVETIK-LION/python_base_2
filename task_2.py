"""
Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
"""


def is_true_predicate(x: int, y: int, z: int):
    """
    Проверяет истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат\n
    :param x: Введите Х
    :param y: Введите Y
    :param z: Введите Z
    :return:
    """
    try:
        if (type(x) != int) or (type(y) != int) or (type(z) != int):
            raise ValueError
    except ValueError:
        return f'Неверное значение. Нужно ввести числа - значения X, Y, Z'

    left = not (x or y or z)
    right = (not x) and (not y) and (not z)

    if left == right:
        return f'Утверждение ВЕРНО'
    else:
        return f'Утверждение НЕ верно'


print(is_true_predicate(-1, 2, 3))
