public class PersonaES2 {
    private String nome;
    private String cognome;
    private int eta;

    public PersonaES2(String nome, String cognome, int eta) {
        this.nome = nome;
        this.cognome = cognome;
        this.eta = eta;
    }

    public void setNome(String nome) {
        this.nome = nome;    
    }
    public String getNome() {
        return nome;
    }
    public void setCognome(String cognome) {
        this.cognome = cognome;
    }
    public String getCognome() {
        return cognome;
    }
    public void setEta(int  eta) {
        this.eta = eta;
    }
    public int getEta() {
        return eta;
    }

    @Override
    public String toString() {
        return "{" +
            " nome='" + getNome() + "'" +
            ", cognome='" + getCognome() + "'" +
            ", eta='" + getEta() + "'" +
            "}";
    }

}
