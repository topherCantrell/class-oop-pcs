public class Robot {
    
    public Robot(String name, int x, int y) {
        System.out.println("ROBOT "+name+""+x+""+y);
    }
    
    public void moveTo(int x, int y) {
        System.out.println("MOVETO "+x+""+y);
    }
    
    public void fireLasers(float power) {
        System.out.println("FIRE "+power);
    }
    
    public float getFuelLevel() {
        System.out.println("GETFUEL");
        return 1.0F;
    }
    
    public static void main(String [] args) {
        
        Robot rob = new Robot("Hank",22,33);
        rob.moveTo(99, 88);
        rob.fireLasers(0.11F);
        float f = rob.getFuelLevel();
        System.out.println(f);
        
    }
    
}