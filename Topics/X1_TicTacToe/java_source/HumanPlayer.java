import java.util.Scanner;

public class HumanPlayer {
	
	private Board brd;	
	private char token;
	private Scanner scn = new Scanner(System.in);

	public HumanPlayer(Board brd, char token) {
		this.brd = brd;		
		this.token = token;
	}
	
	public int getMove() {
		System.out.println(brd);
		while(true) {
			System.out.print("Your move player "+token+": ");
			int move = Integer.parseInt(scn.nextLine());
			if(brd.getCell(move)==' ') {
				return move;
			}
			System.out.println("That spot is taken. Try again.");
		}		
	}
	
}
