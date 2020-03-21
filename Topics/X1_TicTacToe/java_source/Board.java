
public class Board {
	
	private char [] board = {' ',' ',' ',' ',' ',' ',' ',' ',' '};
	
	public Board() {
		clearBoard();
	}
	
	public String toString() {
		String ret = Character.toString(board[0])+"|"+Character.toString(board[1])+"|"+Character.toString(board[2])+"\n";
		ret += "-+-+-\n";
		ret += Character.toString(board[3])+"|"+Character.toString(board[4])+"|"+Character.toString(board[5])+"\n";
		ret += "-+-+-\n";
		ret += Character.toString(board[6])+"|"+Character.toString(board[7])+"|"+Character.toString(board[8]);
		return ret;		
	}
	
	private boolean checkThreeInARow(char token) {
		// Horizontal
		if(board[0]==token && board[1]==token && board[2]==token) return true;
		if(board[3]==token && board[4]==token && board[5]==token) return true;
		if(board[6]==token && board[7]==token && board[8]==token) return true;
		// Vertical
		if(board[0]==token && board[3]==token && board[6]==token) return true;
		if(board[1]==token && board[4]==token && board[7]==token) return true;
		if(board[2]==token && board[5]==token && board[8]==token) return true;
		// Diagonal
		if(board[0]==token && board[4]==token && board[8]==token) return true;
		if(board[2]==token && board[4]==token && board[6]==token) return true;
		return false;
	}
	
	public char getStatus() {
		if(checkThreeInARow('X')) {
			return 'X';
		}
		if(checkThreeInARow('O')) {
			return 'O';
		}
		for(int i=0;i<9;++i) {
			if(board[i]==' ') return ' ';
		}
		return 'C';
	}
	
	public void makeMove(int cell, char token) {
		board[cell] = token;
	}
	
	public char getCell(int cell) {
		return board[cell];
	}
	
	public void clearBoard() {
		for(int i=0;i<9;++i) {
			board[i] = ' ';
		}		
	}

}
