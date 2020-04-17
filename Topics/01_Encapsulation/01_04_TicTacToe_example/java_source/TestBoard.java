import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class TestBoard {

	@Test
	void test_tie() {
		Board board = new Board();
		board.setToken(0,Token.X);
		// MORE HERE
		assertTrue(board.getStatus()==Status.TIE);		
	}
	
	@Test
	void test_x_wins_top_row() {
		Board board = new Board();
		board.setToken(0,Token.X);
		board.setToken(1,Token.X);
		board.setToken(2,Token.X);
		assertTrue(board.getStatus()==Status.WON_X);		
	}

}
