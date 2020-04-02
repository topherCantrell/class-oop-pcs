# We might want to print the board from more than one place ... say again at the end
# of the game. Or we might just want to isolate that one piece of code to make it
# easier to maintain/think-about. Maybe we can test it separately.

# def print_board() # This could simply print the board. Or we could return a
# string representation and let the caller do whatever they want -- print,
# store to disk, text it, other

import random

board = [' '] * 9

def get_board_string():
    
    ret = board[0]+'|'+board[1]+'|'+board[2]+'\n'
    ret = ret + '-+-+-\n'
    ret = ret + board[3]+'|'+board[4]+'|'+board[5]+'\n'
    ret = ret + '-+-+-\n'
    ret = ret + board[6]+'|'+board[7]+'|'+board[8]
    return ret

# The checking for wins is the same for each player ... just a different token. We can make a
# helper function to check all the possibles. Lots of ways to implement the logic. My personal
# favorite is to make a list of triples and run the list. Maybe a loop? Whatever your favorite --
# we are just looking at organization here. 

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

# The main code could call "check_three", but we can make another helper function to
# return the status of the board all at once:
#  'X' - X wins
#  'O' - O wins
#  'C' - Cat (tie)
#  ' ' - Keep playing

# You want to return something different? An integer? An enum might be best (Java, C++)

# Notice how the main loop is easier to read with the verb function calls

def get_board_status():
    if check_for_three_in_a_row('X'):
        return 'X'
    if check_for_three_in_a_row('O'):
        return 'O'    
    for c in board:
        if c == ' ':
            return ' '
    return 'C'        

while True:

    # Print the board
    print(get_board_string())

    # Get the human move
    while True:
        human_move = int(input('Move: '))
        if board[human_move] == ' ':
            break
        print('That spot is taken. Try again.')

    board[human_move] = 'X'
    
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
        if board[computer_move] == ' ':
            break

    board[computer_move] = 'O'

    if get_board_status()=='O':
        print(get_board_string(board))
        print('I win!')
        break
