
public class Magic {


    static int addAll(int ... values) {
        System.out.println(values.length);
        return values[0];
    }

    static int addAll2(int [] values) {
        System.out.println(values.length);
        return values[0];
    }


    public static void main(String [] args) {

        addAll(1,2,3,4);

        int [] vals = {1,2,3,4};
        addAll2(vals);

    }

}