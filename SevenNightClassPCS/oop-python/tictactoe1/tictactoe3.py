# The fact that our board is an array is sprinkled all through the code. What if we ever want to
# change to a 2D array ... or something else? Let's hide the board manipulations behind some
# functions. Encapsulation

import random

board = [' '] * 9

def get_board_string():
    
    ret = board[0]+'|'+board[1]+'|'+board[2]+'\n'
    ret = ret + '-+-+-\n'
    ret = ret + board[3]+'|'+board[4]+'|'+board[5]+'\n'
    ret = ret + '-+-+-\n'
    ret = ret + board[6]+'|'+board[7]+'|'+board[8]
    return ret

def check_for_three_in_a_row(token):
    # Horizontal
    if board[0] == token and board[1] == token and board[2] == token:
        return True
    if board[3] == token and board[4] == token and board[5] == token:
        return True
    if board[6] == token and board[7] == token and board[8] == token:
        return True
    # Vertical
    if board[0] == token and board[3] == token and board[6] == token:
        return True
    if board[1] == token and board[4] == token and board[7] == token:
        return True
    if board[2] == token and board[5] == token and board[8] == token:
        return True
    # Diagonals
    if board[0] == token and board[4] == token and board[8] == token:
        return True
    if board[2] == token and board[4] == token and board[6] == token:
        return True
    # If none
    return False

def get_board_status():
    if check_for_three_in_a_row('X'):
        return 'X'
    if check_for_three_in_a_row('O'):
        return 'O'    
    for c in board:
        if c == ' ':
            return ' '
    return 'C'        

def make_move(cell_number,token):
    # TODO error checking here
    board[cell_number] = token

def get_cell(cell_number):
    return board[cell_number]

def clear_board():
    board = [' '] * 9

while True:

    # Print the board
    print(get_board_string())

    # Get the human move
    while True:
        human_move = int(input('Move: '))
        if get_cell(human_move) == ' ':
            break
        print('That spot is taken. Try again.')

    make_move(human_move,'X')
    
    # Check for wins
    if get_board_status()=='X':
        print(get_board_string())
        print('You win!')
        break
    
    if get_board_status()=='C':
        print(get_board_string())
        print('It is a tie!')
        break

    # Get the computer move
    while True:
        computer_move = random.randint(0, 8)
        if get_cell(computer_move) == ' ':
            break

    make_move(computer_move,'O')

    if get_board_status()=='O':
        print(get_board_string(board))
        print('I win!')
        break
