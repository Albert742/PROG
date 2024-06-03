public class StudenteES2 extends PersonaES2 {
    private String matricola;
    private double media;

    public StudenteES2(String nome, String cognome, int eta, String matricola, double media) {
        super(nome, cognome, eta);
        this.matricola = matricola;
        this.media = media;
        }
    
    public void setMatricola(String matricola) {
        this.matricola = matricola;
    }
    public String getMatricola() {
        return matricola;
    }
    public void setMedia(double media) {
        this.media = media;
    }
    public double getMedia() {
        return media;
    }

    @Override
    public String toString() {
        return "Studente " + super.toString() + ", " + 
            " matricola='" + getMatricola() + "'" +
            ", media='" + getMedia() + "'" +
            "}";
    }
    
}

