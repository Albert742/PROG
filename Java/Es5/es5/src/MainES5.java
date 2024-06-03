public class MainES5 {

    public static void main(String[] args) {
        QuadratoES5 q1 = new QuadratoES5(5);
        System.out.println(q1.area());
        System.out.println(q1.perimetro());

        RettangoloES5 r1 = new RettangoloES5(2, 3);
        System.out.println(r1.area());
        System.out.println(r1.perimetro());

        TriangoloES5 t1 = new TriangoloES5(3, 5,5,5);
        System.out.println(t1.area());
        System.out.println(t1.perimetro());

        TriangoloES5 t2 = new TriangoloES5(5, 5,5,5);
        System.out.println(t2.area());
        System.out.println(t2.perimetro());

        TriangoloES5 t3 = new TriangoloES5(5, 5,7,8);
        System.out.println(t3.area());
        System.out.println(t3.perimetro());
        
    }
}
