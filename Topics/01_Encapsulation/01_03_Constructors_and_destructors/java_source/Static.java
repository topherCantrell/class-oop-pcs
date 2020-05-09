
class Point9 {
    
    static private int numCreated = 0;
    
    static {
        System.out.println("Class loaded");
    }
    
    public static int getNumCreated() {
        return Point9.numCreated;
    }
    
    public Point9() {
        Point9.numCreated = Point9.numCreated + 1;
        System.out.println(Point9.numCreated);
        
        numCreated += 1;
        this.numCreated += 1;
        
    }
    
}


public class Static {
    
    public static void main(String [] args) {
        
        System.out.println("HERE");
        
        System.out.println(Point9.getNumCreated());
        
        Point9 a = new Point9();
        Point9 b = new Point9();
        Point9 c = new Point9();
        
        System.out.println(a.getNumCreated());
        
    }
    
}