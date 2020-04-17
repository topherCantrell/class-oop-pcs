//import java.awt.Point;
import java.util.Date;

class CSVReader {
	public CSVReader(String name) {
		
	}
	
	public String [] getNextRow() {
		String [] ret = new String[5];
		return ret;
	}
	
	public void close() {
		
	}
}

class Robot {
	
	public int location;
	private double battery;
	
	public int getLocation() {
		return location;
	}
	
	public void goTo(int loc) {	
		this.location = loc;
		location = loc;
		battery = battery - 0.10;
	}
	
	
	
	private void moveLeftLeg() {		
	}
	
	private void moveRightLeg() {		
	}	
	
	public void sayHi() {
		System.out.println("Beep Beep");
	}
	
	public double getBatteryLevel() {
		return 0.0;
	}
	
	public void goTo(double lat, double lng) {		
		moveLeftLeg();
		moveRightLeg();
	}
		
}

class TPoint {
	public int x;
	public int y;
	public int getX() {return x;}
	public int getY() {return y;}
	public void setX(int a) {};
}

public class Using {
	
	public static void test(Robot rob) {
		
		int a = rob.getLocation();
		System.out.println(a);
		
		int b = rob.location;
		System.out.println(b);
		
	}
	
	public static void drawLine(int x1, int y1, int x2, int y2) {
		
	}
	
	class Point {asdf
		private int x,y;
		
		public int addX(int a) {
			//return x+a;
			return this.x + a;
		}
	}
	
	
	public static void main(String [] args) {
		
		Point p = new Point();
		
		int a = p.addX(5);
		
		TPoint p = new TPoint();
		
		System.out.println(new Date());
		
		for(int k=0;k<50;++k) {
			for(int j=0;j<1000000000;++j) {
				for(int i=0;i<1000000000;++i) {
					int a = p.getX();
					//int a = p.x;
				}
			}
		}
		
		System.out.println(new Date());
		
		System.exit(0);
						
		p.x = 20;		
		int k = p.x;
		
		p.setX(20);
		int m = p.getX();
		
		
		
		Robot rob = new Robot();
		rob.sayHi();
		double charge = rob.getBatteryLevel();
		rob.goTo(10);
		
		Robot bob = new Robot();
		bob.goTo(20);
		int x = bob.getLocation();
		
		Robot jan = new Robot();
		jan.goTo(50);
		int y = bob.getLocation();
		
		Robot pat = new Robot();
		pat.goTo(50, 20);
		int z = bob.getLocation();
		
		//rob.moveLeftLeg();
				
		//CSVReader csv = new CSVReader("mydata.csv");				
		//String [] row = csv.getNextRow();		
		//csv.close();
		
		
	}
	
}