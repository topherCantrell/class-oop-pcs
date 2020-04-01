
public class TicTacToe {
	
	public static void main(String [] args) {
		
		Board board = new Board();
				
		HumanPlayer player1 = new HumanPlayer();
		HumanPlayer player2 = new HumanPlayer();
		//MrRandom player2 = new MrRandom();
		
		// Who cares what player1 and player2 are?
		// As long as they have "getMove" ...
		
		// No way to say "player2 can be HumanPlayer OR MrRandom". We have to pick
		// a type for variable "player2"
		
		while(true) {
			int move = player1.getMove(board, Token.X);
			board.setToken(move, Token.X);
			if(board.getStatus()!=Status.PLAYING) {
				break;
			}
		
			move = player2.getMove(board,  Token.O);
			board.setToken(move,  Token.O);
			if(board.getStatus()!=Status.PLAYING) {
				break;
			}
		}
		
		System.out.println();
		board.print();
		System.out.println(board.getStatus());		
				
	}

}
