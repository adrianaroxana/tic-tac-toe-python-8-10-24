import os
import random


def init_board():
    """Returns an empty 3-by-3 board (with zeros)."""
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    return board


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row = 3
    col = 3
    valid_moves = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
    move = input('Make your move: ')
    if move.lower() not in valid_moves:
        print('Not a valid move!')
        return get_move(board, player)
    if 'a' in move.lower():
        row = 0
    elif 'b' in move.lower():
        row = 1
    elif 'c' in move.lower():
        row = 2
    if '1' in move.lower():
        col = 0
    elif '2' in move.lower():
        col = 1
    elif '3' in move.lower():
        col = 2
    if board[row][col] != 0:
        print('Place already taken')
        return get_move(board, player)
    return (row, col)


def get_ai_move(board, player):
    '''Returns the coordinates of a valid move for player on board.
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    while board[row][col] != 0:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
    return (row, col)
    '''
    corners = [board[0][0], board[0][2], board[2][0], board[2][2]]
    winning_cases = [[board[0][0], board[0][1], board[0][2]], [board[1][0], board[1][1], board[1][2]],
                     [board[2][0], board[2][1], board[2][2]]]
    winning_cases2 = [[board[0][0], board[1][0], board[2][0]], [board[0][1], board[1][1], board[2][1]],
                      [board[0][2], board[1][2], board[2][2]]]
    winning_cases3 = [board[0][0], board[1][1], board[2][2]]
    winning_cases4 = [board[0][2], board[1][1], board[2][0]]
    for i in winning_cases:
        if sum(i) == 4 and 0 in i:
            row = board.index(i)
            col = i.index(0)
            return(row, col)
    for i in winning_cases2:
        if sum(i) == 4 and 0 in i:
            col = winning_cases2.index(i)
            row = i.index(0)
            return(row, col)
    if sum(winning_cases3) == 4 and 0 in winning_cases3:
        row = winning_cases3.index(0)
        col = winning_cases3.index(0)
        return(row, col)
    if sum(winning_cases4) == 4 and 0 in winning_cases4:
        if winning_cases4.index(0) == 1:
            row, col = 1, 1
            return (row, col)
        elif winning_cases4.index(0) == 0:
            row, col = 0, 2
            return(row, col)
        elif winning_cases4.index(0) == 2:
            row, col = 2, 0
            return(row, col)
    for i in winning_cases:
        if sum(i) == 2 and 1 in i:
            row = board.index(i)
            col = i.index(0)
            return(row, col)
    for i in winning_cases2:
        if sum(i) == 2 and 1 in i:
            col = winning_cases2.index(i)
            row = i.index(0)
            return(row, col)
    if sum(winning_cases3) == 2 and 1 in winning_cases3:
        row = winning_cases3.index(0)
        col = winning_cases3.index(0)
        return(row, col)
    if sum(winning_cases4) == 2 and 1 in winning_cases4:
        if winning_cases4.index(0) == 1:
            row, col = 1, 1
            return (row, col)
        elif winning_cases4.index(0) == 0:
            row, col = 0, 2
            return(row, col)
        elif winning_cases4.index(0) == 2:
            row, col = 2, 0
            return(row, col)
    if board[1][1] == 0:
        row, col = 1, 1
        return(row, col)
    if 0 in corners:
        row = random.randrange(0, 3, 2)
        col = random.randrange(0, 3, 2)
        while board[row][col] != 0:
            row = random.randrange(0, 3, 2)
            col = random.randrange(0, 3, 2)
        return(row, col)
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    while board[row][col] != 0:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
    return (row, col)


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    try:
        if board[row][col] == 0:
            board[row][col] = player
    except IndexError:
        return


def has_won(board, player):
    """Returns True if player has won the game."""
    if (board[0][0] == board[0][1] == board[0][2] == player or board[1][0] == board[1][1] == board[1][2] == player or
        board[2][0] == board[2][1] == board[2][2] == player or board[0][0] == board[1][0] == board[2][0] == player or
        board[0][1] == board[1][1] == board[2][1] == player or board[0][2] == board[1][2] == board[2][2] == player or
            board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player):
        return True
    return False


def is_full(board):
    """Returns True if board is full."""
    if 0 in board[0]:
        return False
    elif 0 in board[1]:
        return False
    elif 0 in board[2]:
        return False
    else:
        return True


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    newboard = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for x in range(len(board)):
        for i in range(len(board[0])):
            if board[x][i] == 0:
                newboard[x][i] = '.'
            if board[x][i] == 1:
                newboard[x][i] = 'X'
            if board[x][i] == 2:
                newboard[x][i] = 'O'
    print('''
               1   2   3
            A  {} | {} | {}
              ---+---+---
            B  {} | {} | {}
              ---+---+---
            C  {} | {} | {}
        '''.format(newboard[0][0], newboard[0][1], newboard[0][2], newboard[1][0], newboard[1][1], newboard[1][2],
                   newboard[2][0], newboard[2][1], newboard[2][2]))


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    if winner == 0:
        print("It's a tie!")
    if winner == 1:
        print('X won!')
    if winner == 2:
        print('O won!')


def tictactoe_game(mode='HUMAN-HUMAN'):
    if mode == 'HUMAN-HUMAN':
        board = init_board()
        while not has_won(board, 1) and not has_won(board, 2) and not is_full(board):
            os.system('cls')
            print_board(board)
            row, col = get_move(board, 1)
            mark(board, 1, row, col)
            os.system('cls')
            print_board(board)
            if not has_won(board, 1) and not is_full(board):
                row, col = get_move(board, 2)
                mark(board, 2, row, col)
                print_board(board)

        if has_won(board, 1):
            winner = 1
        elif has_won(board, 2):
            winner = 2
        else:
            winner = 0
        print_result(winner)
    elif mode == 'HUMAN-AI':
        board = init_board()
        while not has_won(board, 1) and not has_won(board, 2) and not is_full(board):
            os.system('cls')
            print_board(board)
            row, col = get_move(board, 1)
            mark(board, 1, row, col)
            os.system('cls')
            print_board(board)
            if not has_won(board, 1) and not is_full(board):
                row, col = get_ai_move(board, 2)
                mark(board, 2, row, col)
                os.system('cls')
                print_board(board)

        if has_won(board, 1):
            winner = 1
        elif has_won(board, 2):
            winner = 2
        else:
            winner = 0
        print_result(winner)
    elif mode == 'AI-HUMAN':
        pass
    elif mode == 'AI-AI':
        pass


def main_menu():
    '''
    board = [[2, 2, 2],
             [2, 0, 0],
             [2, 2, 2]]
    get_ai_move(board, 2)
    '''
    print('''
      ________________   _________   ______   __________  ______
     /_  __/  _/ ____/  /_  __/   | / ____/  /_  __/ __ \/ ____/
      / /  / // /  ______/ / / /| |/ /  ______/ / / / / / __/
     / / _/ // /__/_____/ / / ___ / /__/_____/ / / /_/ / /___
    /_/ /___/\____/    /_/ /_/  |_\____/    /_/  \____/_____/
        ''')
    print('1.HUMAN-HUMAN')
    print('2.HUMAN-AI')
    print('3.AI-HUMAN')
    print('4.AI-AI')
    select = input('Choose game mode!')
    if select == str(1):
        tictactoe_game('HUMAN-HUMAN')
    elif select == str(2):
        tictactoe_game('HUMAN-AI')
    elif select == str(3):
        tictactoe_game('AI-HUMAN')
    elif select == str(4):
        tictactoe_game('AI-AI')
    else:
        main_menu()


if __name__ == '__main__':
    main_menu()
