"""
Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
"""


def del_some_words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)


my_text = 'абвper per asperaабв aspera aабвd ad asrабвta astra'

print(del_some_words(my_text))
