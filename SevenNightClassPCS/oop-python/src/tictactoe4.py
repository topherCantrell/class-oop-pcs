# Now the player interactions. 

# In tictactoe5 ... do we want just one human player? One computer player? what about different kinds
# of players? Pit two humans or two computers against each other?

# Make player an object. Prompt should say "Your turn player X". Constructor needs the token.
# Is the player locked to a board? Should board be passed in constructor or in get_move?

# If the player has state -- keeping up with where it is in a sequence -- it might be locked to a board.
# If the player uses a giant lookup table from a file, it makes sense to have one player that takes token
# and board.

# Pass the board and token in the constructor