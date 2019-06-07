
public class Clock {
	
	private int hours;
	private int minutes;
	private int seconds;
	
	public Clock(int h, int m, int s) {
		this.hours = h;
		this.minutes = m;
		this.seconds = s;
	}
	
	public int getHours() {
		return this.hours;
	}

	public static void main(String [] args) {
		Clock c = new Clock(23,59,59);
		int h = c.getHours();
		System.out.println(h);
		
		int z = c.minutes + c.seconds;
	}
	
}
