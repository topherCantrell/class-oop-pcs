
public class Point {
	
	private int x = 5;	
	private int y = 6;
	
	{
	    System.out.println("HERE");
	}	
			
	public Point() {
	    x = 7;
        y = 8;
	}
		
	public Point(int x, int y) {		
		this.x = x;
		this.y = y;
	}	
	
	public int getX() {
		return x;
	}
	
	public int getY() {
		return y;
	}	
	
	public boolean equals(Point other) {
	    if(other.x ==x && other.y == y) {
	        return true;
	    }
	    return false;
	}
	
	public static void main(String [] args) {
		
		//Point x = new Point();
		//Point y = new Point(5);
		//Point z = new Point(8,9);
		
		//Point p = new Point(5,2);
		//System.out.println(p.getX());
	    
	    Point a = new Point(1,2);
	    Point b = new Point(1,2);
	    
	   if(a==b) {System.out.println("YES");}
	   
	   if(a.equals(b)) {System.out.println("YEEESSSS");}
	   
	    
		
	}
	
}