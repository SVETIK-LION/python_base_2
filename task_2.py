"""
Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""
"""


from random import randint


print('Привет! Это игра "2021 Конфета".\n'
      'Правила игры:\n'
      '1) На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.\n'
      '2) Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\n'
      '3) Все конфеты оппонента достаются сделавшему последний ход.\n'
      'Кто сделал последний ход - забирает все конфеты и выигрывает!')


def candies_2021_pvp():
    switch = 0
    total_candies = 112
    one_move_max = 28

    player_1 = input('Введите имя первого игрока: ')
    player_2 = input('Введите имя второго игрока: ')

    # Определим, кто будет ходить первым
    first_player = randint(1, 2)
    if first_player == 1:
        first_player = player_1
        second_player = player_2
        print(f'{player_1} ходит первым')
    else:
        first_player = player_2
        second_player = player_1
        print(f'{player_2} ходит первым')

    while total_candies > 0:
        # Ход первого игрока
        if switch == 0:
            move = int(input(f'Сколько конфет берет {first_player}? '))
            if move > one_move_max:
                move = int(input(f'Можно брать не более 28 конфет.\n{first_player}, повторите ввод: '))

            total_candies -= move

        if total_candies > 0:
            switch = 1
            print(f'Осталось еще {total_candies} конфет >o<')
        else:
            print(f'Конфет больше не осталось')

        # Ход второго игрока
        if switch == 1:
            move = int(input(f'Сколько конфет берет {second_player}? '))
            if move > one_move_max:
                move = int(input(f'Можно брать не более 28 конфет.\n{second_player}, повторите ввод: '))

            total_candies -= move

        if total_candies > 0:
            switch = 0
            print(f'Осталось еще {total_candies} конфет >o<')
        else:
            print(f'Совсем не осталось конфет')

    # Выясняем победителя
    if switch == 0:
        print(f'{first_player} - победитель!')
    else:
        print(f'{second_player} - победитель!')


candies_2021_pvp()

