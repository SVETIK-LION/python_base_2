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


def candies_2021_pvp():
    """
    Игра "2021 Конфета" для двух игроков.
    :return:
    """
    switch = 0
    total_candies = 2021
    one_move_max = 28

    print('Привет! Это игра "2021 Конфета".\n'
          'Правила игры:\n'
          '1) На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.\n'
          '2) Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\n'
          '3) Все конфеты оппонента достаются сделавшему последний ход.\n'
          'Кто сделал последний ход - забирает все конфеты и выигрывает!')

    player_1 = input('\nВведите имя первого игрока: ')
    player_2 = input('\nВведите имя второго игрока: ')

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

    # Определяем победителя
    if switch == 0:
        print(f'{first_player} - победитель!')
    else:
        print(f'{second_player} - победитель!')


candies_2021_pvp()


def candies_2021_pvc():
    """
        Игра "2021 Конфета" для одного игрока.
        :return:
        """
    total_candies = 2021
    one_move_max = 28

    print('Привет! Это игра "2021 Конфета".\n'
          'Правила игры:\n'
          '1) На столе лежит 2021 конфета. Вы и компьютер делаете ход друг после друга.\n'
          '2) Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\n'
          '3) Все конфеты оппонента достаются сделавшему последний ход.\n'
          'Кто сделал последний ход - забирает все конфеты и выигрывает!')

    player_1 = input('Как Вас зовут? ')
    player_2 = "Компьютер"
    players = [player_1, player_2]

    # Определим, кто будет ходить первым
    first_player = randint(1, 2)
    print(f'Первым ходит {players[first_player - 1]}')

    while total_candies > 0:
        first_player -= 1
        # Если ходит Компьютер
        if players[first_player % 2] == 'Компьютер':
            print(f'Ходит {players[first_player % 2]}. Осталось {total_candies} конфет(-ы).')

            if total_candies < 29:
                move = total_candies
            else:
                int_part = total_candies // 28
                move = total_candies - ((int_part * one_move_max) + 1)

                if move == -1:
                    move = one_move_max - 1
                elif move == 1:
                    move = one_move_max

            while move < 1 or move > 28:
                move = randint(1, 28)
                if total_candies == 0:
                    print(f'Победил {player_1}')
            print(f'Он берет {move} конфет(-ы).')
        else:
            # Если ходит Игрок
            move = int(input(f'Осталось {total_candies} конфет(-ы). {players[first_player % 2]}, Ваш ход: '))

            while move > one_move_max or move > total_candies:
                move = int(input('Можно брать не более 28 конфет.\n{second_player}, повторите ввод: '))

        total_candies -= move
    print(f'Осталось {total_candies}. {players[first_player % 2]} - победитель!')


candies_2021_pvc()
