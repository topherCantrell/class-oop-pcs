import java.util.Scanner;

public class HumanPlayer {
	
	Scanner in = new Scanner(System.in);
		
	public HumanPlayer() {
		// Maybe a name attribute?
	}
	
	public int getMove(Board board, Token token) {
		board.print();
		System.out.println("Your move player "+token);
		int ret = in.nextInt();
		// @todo error check and loop back
		return ret;		
	}
	
}
