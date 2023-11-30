# Katarenga
This is a pygame emulation of an extremely enjoyable board game named Katarenga (which my friend Piet introduced me to). Katarenga is a close derivative of standard chess played on an 8x8 grid. Running main.py file creates an interactive GUI powered by PyGame for two players to play Katarenga offline. 

# Rules
Each players starts with 8 pieces configured at the rows closest to themselves. Unlike in chess, each piece does not have a predefined set of valid moves. Instead, what ways a piece can move depends on the square that it is currently standing on. In this implementation of the game, the color scheme followed is listed below (though one does not need to refer to since selecting a piece displays its valid moves)
1. RED = King like moves
2. BLUE = Rook like moves
3. GREEN = Bishop like moves
4. BEIGE = Knight like moves

The scatter of the colors at the beginning of the game is (semi)randomized in order to meet some constrains which ensure that one player does not get an immediately advantageous position in the beginning. 

# Winning 
In Katarenga, there is no equivalent of a 'check' or a 'checkmate'. Instead, one wins the game either by capturing all the pieces of the opponent or by advancing two of their own pieces beyond the last row. In this implementation of the game, the way to attempt a piece advancement is to select the piece and scroll-down. If the piece is at the final row, the piece gets advanced and this counts as one move. 

# Known Bugs
As per the rules of Katarenga, one is only allowed to move as far as the next square of the same color. The valid move trajectories however seem to continue beyond this constraint. This is a relatively silly bug hidden somewhere in the code which I haven't gotten around to fixing because I'm currently working on extending the code such that one can play the game online with another player.
   
