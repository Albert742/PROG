class PersonES1 {
    public String name;
    private String surname;
    public int age;
    protected String id;

    public PersonES1(String name, String surname, int age) {
        this.name = name;  
        this.surname = surname;
        this.age = age;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }

    public String getSurname() {
        return surname;
    }
}