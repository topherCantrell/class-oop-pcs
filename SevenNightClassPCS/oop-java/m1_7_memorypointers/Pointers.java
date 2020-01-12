class Point {
	public int x,y,z;
}

class NaPoint extends Point {
	
}

public class Pointers {
	
	public static void pointDouble(Point p) {
		int b = p.x*2;
	    p.x = b;
	    p = new Point();
	    p.x = 10;
	}

	public static void main(String[] args) {
		int b = 3;
		Point a = new Point();
		int c = 4;
		a.x = b;
		a.y = c;
		b = 8;
		pointDouble(a);
		System.out.println(b);
		System.out.println(a.x);
	}

}
