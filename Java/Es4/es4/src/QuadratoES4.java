
public class QuadratoES4 extends FormaGeometrica {

    private double lato;

    public QuadratoES4(double lato) {
        this.lato = lato;
    }

    public double getLato() {
        return this.lato;
    }

    public void setLato(double lato) {
        this.lato = lato;
    }

    @Override
    public double calcolaArea() {
        return lato * lato;
    }
}

