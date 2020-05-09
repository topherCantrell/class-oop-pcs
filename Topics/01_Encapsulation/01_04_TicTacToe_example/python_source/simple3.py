from enum import Enum

class Player(Enum):
    One = 1
    Two = 2

# Show the user the board before asking ... and then reshow with errors? Yes.
def ask_for_move(player):
    print_board()
    move = input('What is your move player '+player.value)
    #move = input('What is your move player '+str(player_num)+'? ')
    #move = input(f'What is your move player {player_num}? ')
    return int(move)

ask_for_move(Player.One)

class BoardStatus(Enum):
    Playing = 'Playing'
    Tie = 'Tie'
    Won_1 = '1 won'
    Won_2 = '2 won'
    
def get_board_sttatus():
    return BoardStatus.Tie


def place_token(move,player_num):
    board[move] = player_num

def check_for_win():
    # Look for 3 tokens in a row ... columns, rows, diagonals
    pass

def has_open_spaces():
    # Look for at least one 0
    pass

def print_board():
    print(board)

# What is a board? Could be just a list of ints: 0=empty, 1=player1, 2=player2

board = [0,0,0,0,0,0,0,0,0] # [0]*9

while True:

    move = ask_for_move(1) # What is move? A number from 0 to 8? "upper left"? Something else? What is a player? Just a number?
    place_token(move,1)   # What does place_token take? an 'X'? a token? a number?
    if check_for_win():
        print('You win player 1')
        break
    
    if not has_open_spaces():
        print('Game is a tie')
        break
    
    move = ask_for_move(2) # What is move? A number from 0 to 8? "upper left"? Something else? What is a player? Just a number?
    place_token(move,2)   # What does place_token take? an 'X'? a token? a number?
    if check_for_win():
        print('You win player 2')
        break
    
print_board() # Maybe inside the loop before each ask_move?
