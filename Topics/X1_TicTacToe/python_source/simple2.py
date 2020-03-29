def ask_for_moveA(is_player_1):
    pass

def ask_for_move(player_num):
    pass

def place_token(move,player_num):
    pass

def check_for_win():
    pass

def get_board_status():
    return 'playing'
    return 'tie'
    return 'won_1'
    return 'won_2'

def has_open_spaces():
    # Why not check_for_tie? Could be, but it is more difficult. You have to
    # check for wins first in that case. A win on the last move is not a tie.
    pass

def print_board():
    pass

while True:
    
    move = ask_for_moveA(True)
    move = ask_for_moveA(is_player_1=True)

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
