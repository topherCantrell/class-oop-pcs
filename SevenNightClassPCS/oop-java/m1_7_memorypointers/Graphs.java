
class Token {
	char letter;
}

class Board {
	Token [] cells;
}

class HumanPlayer {
	Token token;
	Board board;
}

class RandomPlayer {
	Token token;
	Board board;
}

class Game {
	Board board;
	HumanPlayer player1;
	RandomPlayer player2;
}

public class Graphs {
	
	

	public static void main(String[] args) {
		
		Token tokenX = new Token();
		tokenX.letter = 'X';

		Token tokenO = new Token();
		tokenO.letter = 'O';

		Token [] tkns = new Token[9];

		Board brd = new Board();
		brd.cells = tkns;

		HumanPlayer p1 = new HumanPlayer();
		p1.token = tokenX;
		p1.board = brd;

		RandomPlayer p2 = new RandomPlayer();
		p2.token = tokenO;
		p2.board = brd;

		Game gm = new Game();
		gm.board = brd;
		gm.player1 = p1;
		gm.player2 = p2;

		gm.board.cells[2] = gm.player1.token;
		char t = gm.board.cells[2].letter;		
		
		System.out.println(t);

	}

}
