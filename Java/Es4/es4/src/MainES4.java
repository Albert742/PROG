public class MainES4{
    public static void main(String[] args) {
        RettangoloES4 r1 = new RettangoloES4(3.0, 4.0);
        QuadratoES4 q2 = new QuadratoES4(1.0);
        TriangoloES4 t3 = new TriangoloES4(4.0, 3.0);

        System.out.println("Area del RettangoloES4: " + r1.calcolaArea());
        System.out.println("Area del QuadratoES4: " + q2.calcolaArea());
        System.out.println("Area del TriangoloES4: " + t3.calcolaArea());

        r1.setAltezza(5.0);
        System.out.println("Area del RettangoloES4: " + r1.calcolaArea());
    }
}
