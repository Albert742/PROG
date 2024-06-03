public class RettangoloES4 extends FormaGeometrica {

    double base;
    double altezza;

    public RettangoloES4(double base, double altezza) {
        this.base = base;
        this.altezza = altezza ;
    }

    public double getBase() {
        return this.base;
    }

    public void setBase(double base) {
        this.base = base;
    }


    public double getAltezza() {
        return this.altezza;
    }

    public void setAltezza(double altezza) {
        this.altezza = altezza;
    }

    @Override
    public double calcolaArea() {
        return base * altezza;
    }
}
