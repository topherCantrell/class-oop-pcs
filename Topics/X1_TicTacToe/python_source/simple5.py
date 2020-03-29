# What about a game server with multiple games going at the same time? I have "board" as a global. I could
# make board1, board2, etc and pass the board to the functions.

# Notice the 4 functions that work on a board. Remember when we talked about this pattern in the first lesson?
# Passing a pointer to the structure the function should work on? These functions are tied to the board.

# And nobody should be messing with "board" directly (accidentally). I'd like to hide that detail as best I can.

# Lead into the OO design

def ask_for_move(player_num,board):
    print_board(board)
    move = input('What is your move player '+str(player_num)+'? ')
    #move = input(f'What is your move player {player_num}? ')
    return int(move)



def place_token(board, move,player_num):
    board[move] = player_num

def check_for_win(board):
    # Look for 3 tokens in a row ... columns, rows, diagonals
    if board[0]!=0 and board[0]==board[1] and board[0]==board[2]: # top row
        return True
    if board[0]!=0 and board[0]==board[3] and board[0]==board[6]: # left column
        return True
    # TODO: lots more (8 total)
    return False

def has_open_spaces(board):
    for cell in board:
        if cell==0:
            return True
    return False

def print_board(board):
    chars = [' ','X','O']
    print(f'{chars[board[0]]}|{chars[board[1]]}|{chars[board[2]]}')
    print('-+-+-')
    print(f'{chars[board[3]]}|{chars[board[4]]}|{chars[board[5]]}')
    print('-+-+-')
    print(f'{chars[board[6]]}|{chars[board[7]]}|{chars[board[8]]}')

# What is a board? Could be just a list of ints: 0=empty, 1=player1, 2=player2

board1 = [0,0,0,0,0,0,0,0,0] # [0]*9
board2 = [0]*9
board3 = [0]*9

while True:

    move = ask_for_move(1,board1) # What is move? A number from 0 to 8? "upper left"? Something else? What is a player? Just a number?
    place_token(board1,move,1)   # What does place_token take? an 'X'? a token? a number?
    if check_for_win(board1):
        print('You win player 1')
        break
    
    if not has_open_spaces(board1):
        print('Game is a tie')
        break
    
    move = ask_for_move(2,board1) # What is move? A number from 0 to 8? "upper left"? Something else? What is a player? Just a number?
    place_token(board1,move,2)   # What does place_token take? an 'X'? a token? a number?
    if check_for_win(board1):
        print('You win player 2')
        break
    
print_board(board1) # Maybe inside the loop before each ask_move?
