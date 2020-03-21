# We don't need "random" in the main anymore. MrRandom needs it ... nobody
# else needs to worry about it

import random

class MrRandom:
    
    def __init__(self, token, board):        
        self._board = board
     
    def get_move(self):   
        while True:
            computer_move = random.randint(0, 8)
            if self._board.get_cell(computer_move) == ' ':
                return computer_move