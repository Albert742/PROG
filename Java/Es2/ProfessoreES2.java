class ProfessoreES2 extends PersonaES2 {
    private String materia;
    private int salario;
    
    public ProfessoreES2(String nome, String cognome, int eta, String materia, int salario) {
        super(nome, cognome, eta);
        this.materia = materia;
        this.salario = salario;
    }
    public void setMateria(String materia) {
        this.materia = materia;
    }
    public String getMateria() {
        return materia;
    }
    public void setSalario(int salario) {
        this.salario = salario;
    }
    public int getSalario() {
        return salario;
    }

    @Override
    public String toString() {
        return "Professore " + super.toString() + "," + 
            " materia='" + getMateria() + "'" +
            ", salario='" + getSalario() + "'" +
            "} ";
    }
}

