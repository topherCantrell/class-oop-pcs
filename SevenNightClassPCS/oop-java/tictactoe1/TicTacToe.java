
public class TicTacToe {
	
	public static void main(String [] args) {
		
		Board brd = new Board();
		HumanPlayer player1 = new HumanPlayer(brd,'X');
		MrRandom player2 = new MrRandom(brd,'O');
		String status = "";
		
		while(true) {
			int move = player1.getMove();
			brd.makeMove(move, 'X');
			
			if(brd.getStatus()=='X') {
				status = "Player X wins!";
				break;
			}
			
			if(brd.getStatus()=='C') {
				status = "It is a Tie!";
				break;
			}
			
			move = player2.getMove();
			brd.makeMove(move, 'O');
			
			if(brd.getStatus()=='O') {
				status = "Player O wins!";
				break;
			}
		}
		
		System.out.println(brd);
		System.out.println(status);
		
	}

}
