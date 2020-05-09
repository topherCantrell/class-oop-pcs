class Point2 {
    
    public static final int ME = 22;
    
    private final int x = 0;
    
    private final int y;
    
    private int z = 2;
    
    //private final int z;
    
    public Point2() {
        
        y = 5;
        
    }
    
    public void tell() {
        System.out.println(x);
        System.out.println(y);
        System.out.println(z);
        System.out.println(ME);
    }
    
    public void finalize() {
        System.out.println("Here in finalize");
    }
        
}


public class Fin {
    
    public static void main(String [] args) {
        
        Point p = new Point();
        
        p = null;
        
        p = new Point();
        
        System.out.println("Last line of program");
        
    }
    
}