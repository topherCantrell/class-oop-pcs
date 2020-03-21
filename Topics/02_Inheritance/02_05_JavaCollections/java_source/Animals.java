import java.util.ArrayList;
import java.util.List;

interface Animal {
	public void sayHi();
}

class Cat implements Animal {
	public void sayHi() {
		System.out.println("Meow!");		
	}	
}

class Dog implements Animal {
	public void sayHi() {
		System.out.println("Woof!");
	}	
}

public class Animals {
	
	public static void speak(Animal an) {
		an.sayHi();
	}
	
	public static void useList() {
		
		List names = new ArrayList();		
		
		names.add("Sam");
		names.add("Jan");
		
		String bob = "Bob";
		Object o = bob;
		
		names.add(o);
		
		String n = (String) names.get(1);
		
		System.out.println(names.get(1));
		System.out.println(names.get(2));		
		
		names.add(1,"Sue");
		
		System.out.println(names.get(0));
		System.out.println(names.get(1));
		
		System.out.println("There are "+names.size()+" items.");
		
	}
	
	public static void main(String [] args) {
		
		//useList();
		
		List<Integer> nums = new ArrayList<Integer>();
		
		nums.add(0);
		int a = nums.get(0);
		
		nums.add(null);
		int b = nums.get(1);
		
		
		List<Animal> zoo = new ArrayList<Animal>();
		
		Cat cat = new Cat();
		Dog dog = new Dog();
		
		speak(dog);
		
		zoo.add(cat);
		zoo.add(dog);
		
		Animal an = zoo.get(0);
		an.sayHi();
		
		an = zoo.get(1);
		an.sayHi();
		
	}

}
