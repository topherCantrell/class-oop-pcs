
def ask_for_move(player_num):
    print_board()
    move = input('What is your move player '+str(player_num)+'? ')
    #move = input(f'What is your move player {player_num}? ')
    return int(move)

def place_token(move,player_num):
    board[move] = player_num

def get_board_status():
    # Look for 3 tokens in a row ... columns, rows, diagonals
    if board[0]==1 and board[0]==board[1] and board[0]==board[2]: # top row
        return 'won_1'
    if board[0]==2 and board[0]==board[3] and board[0]==board[6]: # left column
        return 'won_2'
    # return 'tie'
    return 'playing'

def print_board():
    print(board)

# What is a board? Could be just a list of ints: 0=empty, 1=player1, 2=player2

board = [0,0,0,0,0,0,0,0,0] # [0]*9

class Board:
    
    def __init__(self):
        self.cells = [0]*9
        
    def place_token(self,move,player):
        self.cells[move] = player
        
    def get_board_status(self):
        pass
    
    def print_board(self):
        print(self.cells)
        
board = Board()
board.place_token(move,player)

playing = True
while playing:
    
    for player in [1,2]:
        
        move = ask_for_move(player)
        
        place_token(move,player)
         
        status = get_board_status()        
        if status == 'won_1':
            print('Player 1 won')
            playing = False
            break            
        elif status == 'won_2':
            print('Player 2 won')
            playing = False
            break
        elif status == 'tie':
            print('It is a tie')
            playing = False
            break        
    
print_board() # Maybe inside the loop before each ask_move?
