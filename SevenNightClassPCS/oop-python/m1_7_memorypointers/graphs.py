class Token:
    pass
    #char letter

class Board:
    pass
    #Token [] cells;

class HumanPlayer:
    pass
    #Token token
    #Board board

class RandomPlayer:
    pass
    #Token token
    #Board board

class Game:
    pass
    #Board board
    #HumanPlayer player1
    #RandomPlayer player2
    
tokenX = Token();
tokenX.letter = 'X';

tokenO = Token();
tokenO.letter = 'O';

tkns = [None]*9;

brd = Board();
brd.cells = tkns;

p1 = HumanPlayer();
p1.token = tokenX;
p1.board = brd;

p2 = RandomPlayer();
p2.token = tokenO;
p2.board = brd;

gm = Game();
gm.board = brd;
gm.player1 = p1;
gm.player2 = p2;

gm.board.cells[2] = gm.player1.token;
t = gm.board.cells[2].letter;        

print(t)