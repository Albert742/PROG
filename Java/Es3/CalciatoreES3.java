public class CalciatoreES3 extends PersonaES3 {
    private String ruolo;
    private int numeroMaglia;
    private String squadra;


    public CalciatoreES3(String nome, String cognome, String ruolo, int numeroMaglia, String squadra) {
        super(nome, cognome);
        this.ruolo = ruolo;
        this.numeroMaglia = numeroMaglia;
        this.squadra = squadra;
    }


    public String getRuolo() {
        return this.ruolo;
    }

    public void setRuolo(String ruolo) {
        this.ruolo = ruolo;
    }

    public int getNumeroMaglia() {
        return this.numeroMaglia;
    }

    public void setNumeroMaglia(int numeroMaglia) {
        this.numeroMaglia = numeroMaglia;
    }

    public String getSquadra() {
        return this.squadra;
    }

    public void setSquadra(String squadra) {
        this.squadra = squadra;
    }

    @Override
    public String toString() {
        return "Calciatore " +
        super.toString() + "," +
        " ruolo='" + getRuolo() + "'" +
        ", numeroMaglia='" + getNumeroMaglia() + "'" +
        ", squadra='" + getSquadra() + "'" +
        "}";
    }

}
