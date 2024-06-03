public class PersonaES3 {
    private String nome;
    private String cognome;
    
    public PersonaES3(String nome, String cognome) {
        this.nome = nome;
        this.cognome = cognome;
    }
    
    public String getNome() {
        return nome;
    }
    
    public void setNome(String nome) {
        this.nome = nome;
    }
    
    public String getCognome() {
        return cognome;
    }
    
    public void setCognome(String cognome) {
        this.cognome = cognome;
    }

    @Override
    public String toString() {
        return "{" +
            " nome='" + getNome() + "'" +
            ", cognome='" + getCognome() + "'" +
            "}";
    }
}
