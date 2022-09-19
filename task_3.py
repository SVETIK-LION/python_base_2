"""
Создайте программу для игры в ""Крестики-нолики"".
"""


new_board = list(range(1, 10))


def draw_board(board):
    """
    Чертит доску для игры
    :param board:
    :return:
    """
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)


def write_symbol(player_symbol):
    valid = False
    while not valid:
        player_answer = input(f'Куда поставить {player_symbol}? ')
        try:
            player_answer = int(player_answer)
        except ValueError:
            print("Неверное значение. Нужно ввести номер клетки от 1 до 9")
            continue

        if 1 <= player_answer <= 9:
            if str(new_board[player_answer - 1]) not in "XO":
                new_board[player_answer-1] = player_symbol
                valid = True
            else:
                print("Клетка уже занята, выберете другую")
        else:
            print("Неверное значение. Нужно ввести номер клетки от 1 до 9")


def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


def tic_tac_toe(board):
    counter = 0
    win = True
    while win:
        draw_board(board)
        if counter % 2 == 0:
            write_symbol("X")
        else:
            write_symbol("O")
        counter += 1
        if counter > 4:
            win_symbol = check_win(board)
            if win_symbol:
                print(f'{win_symbol}, "выиграл!')
                break
        if counter == 9:
            print("Победила дружба! Ничья :)")
            break
    draw_board(board)


tic_tac_toe(new_board)
