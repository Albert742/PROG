public class QuadratoES5 implements Calcolo{
    double lato;

    public QuadratoES5(double lato) {
        this.lato = lato;
    }
    
    public double getLato() {
        return lato;
    }
    
    public void setLato(double lato) {
        this.lato = lato;
    }
    
    @Override
    public double area() {
        return lato * lato;
    }
    
    @Override
    public double perimetro() {
        return lato * 4;
    }

}
