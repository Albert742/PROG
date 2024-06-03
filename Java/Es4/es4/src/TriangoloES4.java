public class TriangoloES4 extends FormaGeometrica {

    double base;
    double altezza;

    public TriangoloES4(double base, double altezza) {
        this.base = base;
        this.altezza = altezza;
    }

    public double getBase() {
        return this.base;
    }

    public void setBase(double base) {
        this.base = base;
    }


    @Override
    public double calcolaArea() {
        return (base * altezza) / 2;
    }
}


