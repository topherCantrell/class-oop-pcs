class Point {
	int x;
	int y;
}

class Line {
	Point a;
	Point b;
}

class TTTBoard {
	Line h1;
	Line h2;
	Line v1;
	Line v2;
}

public class Struct {	
	
	public static void main(String [] args) {
		
		int j = 0xBE025F20;
						
		Point p = new Point();
		p.x = 2;
		p.y = 3;
		
		Line g = new Line();
		g.a = new Point();
		g.b = new Point();
		g.a.x = 4;
		g.b.y = 5;

		TTTBoard board = new TTTBoard();
		board.h1 = new Line();
		board.h1.a = new Point();
		board.h1.b = new Point();
		board.h1.a.x = 3;
		
		Point i = new Point();
		Line w = new Line();
		w.a = i;
		w.b = i;
		
		w.a.x = 20;   // Set point a's X to 20
		w.b.x = 1000; // Set point b's X to 1000
		
		// What was point a's X again?
		System.out.println(w.a.x);
		// 1000? What the heck?
		
		
		System.out.println("Hello");
		
	}
	
}