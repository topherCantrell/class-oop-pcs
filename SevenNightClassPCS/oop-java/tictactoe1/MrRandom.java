import java.util.Random;

public class MrRandom {
	
	private Board brd;
	private Random rnd = new Random();

	public MrRandom(Board brd, char token) {
		this.brd = brd;		
	}
	
	public int getMove() {		
		while(true) {
			int move = rnd.nextInt(9);
			if(brd.getCell(move)==' ') {
				return move;
			}
		}		
	}

}
