"""
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
"""


def compress_data(data: str):
    count = 1
    result = ''
    for i in range(len(data) - 1):
        if data[i] == data[i + 1]:
            count += 1
        else:
            result = result + str(count) + data[i]
            count = 1
    if count > 1 or (data[len(data) - 2] != data[-1]):
        result = result + str(count) + data[-1]

    return result


def recover_data(compressed_data):
    number = ''
    result = ''
    for i in range(len(compressed_data)):
        if not compressed_data[i].isalpha():
            number += compressed_data[i]
        else:
            result = result + compressed_data[i] * int(number)
            number = ''

    return result


with open('data.txt', 'w') as f:
    f.write('Пароль')

with open('data.txt', 'r') as f:
    my_data = f.read()

with open('compress_data.txt', 'w') as f:
    f.write(compress_data(my_data))

with open('compress_data.txt', 'r') as f:
    compr_data = f.read()


print(f'Сжатые данные: {compr_data}')
print(f'Восстановленные данные: {recover_data(compress_data(my_data))}')
