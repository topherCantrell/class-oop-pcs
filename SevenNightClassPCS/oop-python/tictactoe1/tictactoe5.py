# Now the player interactions. 

# In tictactoe5 ... do we want just one human player? One computer player? what about different kinds
# of players? Pit two humans or two computers against each other?

# Make player an object. Prompt should say "Your turn player X". Constructor needs the token.
# Is the player locked to a board? Should board be passed in constructor or in get_move?

# If the player has state -- keeping up with where it is in a sequence -- it might be locked to a board.
# If the player uses a giant lookup table from a file, it makes sense to have one player that takes token
# and board.

# Pass the board and token in the constructor

# The board is a global variable in our code. There is exactly one board in existence.
# Do we ever want to handle more than one board at a time? Maybe a server managing
# several games at once?
#
# We can encapsulate all the board logic and private parts within a Board class

# The fact that our board is an array is sprinkled all through the code. What if we ever want to
# change to a 2D array ... or something else? Let's hide the board manipulations behind some
# functions. Encapsulation

# We'll create a Player baseclass when we get to inheritance next module

from board import Board
from human import HumanPlayer
from mr_random import MrRandom

brd = Board()
#player_1 = HumanPlayer('X',brd)
player_1 = MrRandom('X',brd)
player_2 = MrRandom('O',brd)

# The logic below doesn't care what player_1 and player_2 are. It just
# uses whatever is created. Try two humans. Or let MrRandom go first.
# Could ask the user to configure the game.

while True:    

    # Get player 1's move
    move = player_1.get_move()
    brd.make_move(move,'X')
    
    # Check for wins
    if brd.get_status()=='X':
        status = 'Player X wins!'        
        break
    
    if brd.get_status()=='C':
        status = 'It is a Tie!'
        break

    # Get the computer move
    move = player_2.get_move()    
    brd.make_move(move,'O')

    if brd.get_status()=='O':
        status = 'Player O wins!'
        break

print(brd.get_string_repr())
print(status)