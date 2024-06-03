public class RettangoloES5 implements Calcolo {

    double base;
    double altezza;

    public RettangoloES5(double base, double altezza) {
        this.base = base;
        this.altezza = altezza;
    }

    public double getBase() {
        return base;
    }

    public void setBase(double base) {
        this.base = base;  
    }

    public double getAltezza() {
        return altezza;
    }

    @Override   
    public double area() {
        return base * altezza;
    }

    @Override
    public double perimetro() {
        return (base + altezza) * 2;
    }
}
