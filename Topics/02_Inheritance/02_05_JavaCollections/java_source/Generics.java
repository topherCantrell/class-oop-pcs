import java.awt.Point;
import java.util.ArrayList;
import java.util.List;

public class Generics {
	
	public static void plain() {
		List items = new ArrayList();		
		items.add("Hello");				
		String a = (String) items.get(0);				
		System.out.println(a);				
	}
	
	public static void withGenerics() {
		List<String> items = new ArrayList<String>();		
		items.add("HELLO");		
		String a = items.get(0);		
		System.out.println(a);
	}
	
	public static void diff() {
		List items = new ArrayList();	
		items.add("hello");
		items.add(45);
		items.add(new Point(1,2));
		
		Point p = (Point) items.get(2);
		int a = (int) items.get(1);
		String b = (String) items.get(0);
		
		Object o = items.get(1);
		if(o instanceof String) { }
	}
	
	public static void main(String [] args) {
				
		plain();
		withGenerics();
		diff();
		
	}

}
