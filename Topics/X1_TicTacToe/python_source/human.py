
class HumanPlayer:
    
    def __init__(self, token, board):
        self._token = token
        self._board = board
        
    def get_move(self):
        # Print the board so the human can see the options
        print(self._board.get_string_repr())
        while True:
            human_move = int(input('Your move player '+self._token+': '))
            if self._board.get_cell(human_move) == ' ':
                return human_move
            print('That spot is taken. Try again.')