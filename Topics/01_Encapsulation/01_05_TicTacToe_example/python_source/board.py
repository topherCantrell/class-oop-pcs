
class Board:
    
    def __init__(self):
        self.clear_board()
        
    def get_string_repr(self):
        ret = self._board[0]+'|'+self._board[1]+'|'+self._board[2]+'\n'
        ret = ret + '-+-+-\n'
        ret = ret + self._board[3]+'|'+self._board[4]+'|'+self._board[5]+'\n'
        ret = ret + '-+-+-\n'
        ret = ret + self._board[6]+'|'+self._board[7]+'|'+self._board[8]
        return ret
    
    # This is for our private use. Outsiders shouldn't need it.
    def _check_for_three_in_a_row(self,token):
        # Horizontal
        if self._board[0] == token and self._board[1] == token and self._board[2] == token:
            return True
        if self._board[3] == token and self._board[4] == token and self._board[5] == token:
            return True
        if self._board[6] == token and self._board[7] == token and self._board[8] == token:
            return True
        # Vertical
        if self._board[0] == token and self._board[3] == token and self._board[6] == token:
            return True
        if self._board[1] == token and self._board[4] == token and self._board[7] == token:
            return True
        if self._board[2] == token and self._board[5] == token and self._board[8] == token:
            return True
        # Diagonals
        if self._board[0] == token and self._board[4] == token and self._board[8] == token:
            return True
        if self._board[2] == token and self._board[4] == token and self._board[6] == token:
            return True
        # If none
        return False

    def get_status(self):
        if self._check_for_three_in_a_row('X'):
            return 'X'
        if self._check_for_three_in_a_row('O'):
            return 'O'    
        for c in self._board:
            if c == ' ':
                return ' '
        return 'C'        

    def make_move(self,cell_number,token):
        # TODO error checking here
        self._board[cell_number] = token
    
    def get_cell(self,cell_number):
        return self._board[cell_number]
    
    def clear_board(self):
        self._board = [' '] * 9
