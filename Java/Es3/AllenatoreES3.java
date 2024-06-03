public class AllenatoreES3 extends PersonaES3 {
    private int salario;

    public AllenatoreES3(String nome, String cognome, int salario) {
        super(nome, cognome);
        this.salario = salario;
    }


    public int getSalario() {
        return this.salario;
    }

    public void setSalario(int salario) {
        this.salario = salario;
    }

    @Override
    public String toString() {
        return "Allenatore " +
        super.toString() + "," +
        " salario='" + getSalario() + "'" +
        "}";
    }

}
