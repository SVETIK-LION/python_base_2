"""
Напишите программу, которая по заданному номеру четверти,
показывает диапазон возможных координат точек в этой четверти (x и y).
"""


def range_by_quarter(quarter: int):
    """
    По номеру четверти тригонометрического круга определяет диапазон точек\n
    :param quarter: Номер четверти
    :return:
    """
    try:
        if quarter == 1:
            return f'x ∈ (0, ∞)\ny ∈ (0, ∞)'
        elif quarter == 2:
            return f'x ∈ (-∞, 0)\ny ∈ (0, ∞)'
        elif quarter == 3:
            return f'x ∈ (-∞, 0)\ny ∈ (-∞, 0)'
        elif quarter == 4:
            return f'x ∈ (0, ∞)\ny ∈ (-∞, 0)'
        else:
            if quarter < 1 or quarter > 4 or type(quarter) != int:
                return f'Номер плоскости - это целое число от 1 до 4'
    except TypeError:
        return f'Неверное значение. Нужно ввести число - номер плоскости (от 1 до 4)'


print(range_by_quarter(4))
