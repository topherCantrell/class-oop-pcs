import random

board = [' '] * 9

while True:

    # Print the board
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])

    # Get the human move
    while True:
        human_move = int(input('Move: '))
        if board[human_move] == ' ':
            break
        print('That spot is taken. Try again.')

    board[human_move] = 'X'
    
    # Check for wins
    if board[0] == 'X' and board[1] == 'X' and board[2] == 'X':
        # A LOT more options
        print('You win!')
        break
    
    # Check for tie
    cat = True
    for c in board:
        if c == ' ':
            cat = False
            break

    if cat:
        print('It is a tie!')
        break

    # Get the computer move
    while True:
        computer_move = random.randint(0, 8)
        if board[computer_move] == ' ':
            break

    board[computer_move] = 'O'

    if board[0] == 'O' and board[1] == 'O' and board[2] == 'O':
        # A LOT more options
        print('I win!')
        break
