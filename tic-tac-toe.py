import sys
import random
import os

def init_board():
    """Returns an empty 3-by-3 board (with zeros)."""
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    return board


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    player_move = input("Choose your move: ").upper()
    valid_input = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
    valid_input_length = 2
    while player_move:
        if player_move.upper() == "QUIT":
            sys.exit()
        elif len(player_move) != valid_input_length: 
            player_move = input("Please choose a valid move: ").upper()
        elif player_move not in valid_input:
            player_move = input("Your coordinates should be between A1 and C3. Please choose a new move ").upper()
        else:
            row = ord(player_move[0]) - 65
            col = ord(player_move[1]) - 49
            
            # if 'A' in player_move.upper():
            #     row = 0
            # elif 'B' in player_move.upper():
            #     row = 1
            # elif 'C' in player_move.upper():
            #     row = 2
            # if '1' in player_move:
            #     col = 0
            # elif '2' in player_move:
            #     col = 1
            # elif '3' in player_move:
            #     col = 2
            if board[row][col] != 0:
                print('Place already taken')
                return get_move(board, player)
        return row, col


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    while board[row][col] != 0:    
        row = random.randint(0, 2)
        col = random.randint(0, 2)
    return (row, col)


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    if board[row][col] == 0:
        board[row][col] = player


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
    while (0 not in board[0]) and (0 not in board[1]) and (0 not in board[2]):
        return True
    return False


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    newboard = [[0,0,0], [0,0,0], [0,0,0]]
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                newboard[row][col] = '.'
            if board[row][col] == 1:
                newboard[row][col] = 'X'
            if board[row][col] == 2:
                newboard[row][col] = 'O'  
    print('   1' + '   2' + '   3')
    print('A  ' + str(newboard[0][0]) + ' | ' + str(newboard[0][1]) + ' | ' + str(newboard[0][2]))
    print('  ---+---+---')
    print('B  ' + str(newboard[1][0]) + ' | ' + str(newboard[1][1]) + ' | ' + str(newboard[1][2]))
    print('  ---+---+---')
    print('C  ' + str(newboard[2][0]) + ' | ' + str(newboard[2][1]) + ' | ' + str(newboard[2][2]))


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    if winner == 0:
        print('''
  _____ _______ _  _____                 _______ _____ ______ 
 |_   _|__   __( )/ ____|       /\      |__   __|_   _|  ____|
   | |    | |  |/| (___        /  \        | |    | | | |__   
   | |    | |     \___ \      / /\ \       | |    | | |  __|  
  _| |_   | |     ____) |    / ____ \      | |   _| |_| |____ 
 |_____|  |_|    |_____/    /_/    \_\     |_|  |_____|______|
                                                              
                                                              

    ''')
    if winner == 1:
        print('''
    __  __   __        _____  _   _ 
    \ \/ /   \ \      / / _ \| \ | |
     \  /     \ \ /\ / / | | |  \| |
     /  \      \ V  V /| |_| | |\  |
    /_/\_\      \_/\_/  \___/|_| \_|
                                

    ''')        
    if winner == 2:
        print('''
   ___    __          ______  _   _ 
  / _ \   \ \        / / __ \| \ | |
 | | | |   \ \  /\  / / |  | |  \| |
 | | | |    \ \/  \/ /| |  | | . ` |
 | |_| |     \  /\  / | |__| | |\  |
  \___/       \/  \/   \____/|_| \_|
                                   
                                   

    ''')


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
        other_menu()
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
        other_menu()
    elif mode == 'AI-HUMAN':
        board = init_board()
        while not has_won(board, 1) and not has_won(board, 2) and not is_full(board):
            row, col = get_ai_move(board, 2)
            mark(board, 1, row, col)
            os.system('cls')
            print_board(board)
            if not has_won(board, 1) and not is_full(board):
                row, col = get_move(board, 1)
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
        other_menu()


def other_menu():
    user_answer = input("Do you want to play again?").upper()
    if user_answer == "YES":
        main_menu()
    else:
        sys.exit()

def main_menu():
    print('''
      ________________   _________   ______   __________  ______
     /_  __/  _/ ____/  /_  __/   | / ____/  /_  __/ __ \/ ____/
      / /  / // /  ______/ / / /| |/ /  ______/ / / / / / __/
     / / _/ // /__/_____/ / / ___ / /__/_____/ / / /_/ / /___
    /_/ /___/\____/    /_/ /_/  |_\____/    /_/  \____/_____/
        ''')

    print("Welcome!")
    print("If you want to play HUMAN-HUMAN press 1")
    print("If you want to play HUMAN-AI, press 2")
    print("If you want to play AI-HUMAN, press 3")
    print("If you want to close the game, type \"quit\"")

    choose = (input('Choose game mode!')).upper()
    if choose == 'QUIT':
        sys.exit()
    elif choose == "1":
        tictactoe_game('HUMAN-HUMAN')
    elif choose == "2":
        tictactoe_game('HUMAN-AI')
    elif choose == "3":
        tictactoe_game('AI-HUMAN')
    else:
        main_menu()


if __name__ == '__main__':
    main_menu()
