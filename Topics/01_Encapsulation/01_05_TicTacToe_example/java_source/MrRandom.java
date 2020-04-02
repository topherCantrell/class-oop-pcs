import java.util.Random;

public class MrRandom {
		
	private Random rnd = new Random();

	public MrRandom() {			
	}
	
	public int getMove(Board board, Token token) {		
		while(true) {
			int move = rnd.nextInt(9);
			if(board.getToken(move)==Token.NONE) {
				return move;
			}
		}		
	}

}
