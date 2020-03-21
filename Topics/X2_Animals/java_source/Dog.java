// public class implements Animal {
public class Dog extends Animal {
	
	@Override
	public void sayHi() {
		System.out.println("Bark Bark!");
	}
		
	public static void main(String [] args) {
		Animal p = new Dog();
		p.sayHi();
		
	}
}
