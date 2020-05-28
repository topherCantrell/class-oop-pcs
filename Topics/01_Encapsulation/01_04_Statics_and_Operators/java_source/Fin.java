class Point2 {
    
    private final int x = 0;
    
    private final int y;
    
    //private final int z;
    
    public Point2() {
        
        y = 5;
        
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