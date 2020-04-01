
public class Board {
	
	private Token [] board = {
			Token.NONE,Token.NONE,Token.NONE,
			Token.NONE,Token.NONE,Token.NONE,
			Token.NONE,Token.NONE,Token.NONE};
	
	public Board() {		
	}
	
	public void newGame() {
		for(int i=0;i<9;++i) {
			board[i] = Token.NONE;
		}
	}
	
	public void setToken(int cell, Token token) {
		board[cell] = token;
	}
	
	public Token getToken(int cell) {
		return board[cell];
	}
	
	private boolean check_tripples(Token token) {
		if(board[0]==token && board[1]==token && board[2]==token) return true;
		if(board[3]==token && board[4]==token && board[5]==token) return true;
		if(board[6]==token && board[7]==token && board[8]==token) return true;
		if(board[0]==token && board[3]==token && board[6]==token) return true;
		if(board[1]==token && board[4]==token && board[7]==token) return true;
		if(board[2]==token && board[5]==token && board[8]==token) return true;
		if(board[0]==token && board[4]==token && board[8]==token) return true;
		if(board[2]==token && board[4]==token && board[6]==token) return true;
		return false;
	}
	
	public Status getStatus() {
		if(check_tripples(Token.X)) return Status.WON_X;
		if(check_tripples(Token.O)) return Status.WON_O;
		for(int i=0;i<9;++i) {
			if(board[i] == Token.NONE) return Status.PLAYING;
		}
		return Status.TIE;
	}
	
	private String tokenToString(Token token) {
		switch(token) {
		case O:
			return "O";
		case X:
			return "X";
		default:
			return " ";
		}
	}
	
	public void print() {
		System.out.println(tokenToString(board[0])+"|"+tokenToString(board[1])+"|"+tokenToString(board[2]));
		System.out.println("-+-+-");
		System.out.println(tokenToString(board[3])+"|"+tokenToString(board[4])+"|"+tokenToString(board[5]));
		System.out.println("-+-+-");
		System.out.println(tokenToString(board[6])+"|"+tokenToString(board[7])+"|"+tokenToString(board[8]));
	}	
	
}
