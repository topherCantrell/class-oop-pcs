# The board is a global variable in our code. There is exactly one board in existence.
# Do we ever want to handle more than one board at a time? Maybe a server managing
# several games at once?
#
# We can encapsulate all the board logic and private parts within a Board class

# The fact that our board is an array is sprinkled all through the code. What if we ever want to
# change to a 2D array ... or something else? Let's hide the board manipulations behind some
# functions. Encapsulation

import random

import board

brd = board.Board()
# from board import Board
# brd = Board()

# Notice how we ask the board object to do things.

while True:

    # Print the board
    print(brd.get_string_repr())

    # Get the human move
    while True:
        human_move = int(input('Move: '))
        if brd.get_cell(human_move) == ' ':
            break
        print('That spot is taken. Try again.')

    brd.make_move(human_move,'X')
    
    # Check for wins
    if brd.get_status()=='X':
        print(brd.get_string_repr())
        print('You win!')
        break
    
    if brd.get_status()=='C':
        print(brd.get_string_repr())
        print('It is a tie!')
        break

    # Get the computer move
    while True:
        computer_move = random.randint(0, 8)
        if brd.get_cell(computer_move) == ' ':
            break

    brd.make_move(computer_move,'O')

    if brd.get_status()=='O':
        print(brd.get_string_repr())
        print('I win!')
        break
