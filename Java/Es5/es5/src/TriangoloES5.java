public class TriangoloES5 implements Calcolo{
    double base;
    double altezza;
    double lato1;
    double lato2;

    public TriangoloES5(double base, double altezza, double lato1, double lato2) {
        this.base = base;
        this.altezza = altezza;
        this.lato1 = lato1;
        this.lato2 = lato2;
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

    public void setAltezza(double altezza) {
        this.altezza = altezza;
    }

    public double getLato1() {
        return lato1;
    }

    @Override
    public double area() {
        return (base * altezza) / 2;
    }

    @Override
    public double perimetro() {
        if (lato1 == lato2 && lato2 == base) {
            return lato1 * 3;
        } 
        else if (lato1 == lato2 && lato2 != base) {
            return (lato1 * 2 )+ base;
        }
        else {
            return lato1 + lato2 + base; 
        }
    }
}
