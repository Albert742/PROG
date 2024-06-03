public class MainES2 {
    public static void main(String[] args) {
        StudenteES2 s1 = new StudenteES2("Gianni", "Dei", 19, "0000", 7);
        ProfessoreES2 p1 = new ProfessoreES2("Mario", "Rossi", 34, "Matematica", 1250);
        StudenteES2 s2 = new StudenteES2("Caio", "Totti", 19, "0001", 8.4);

        System.out.println(p1.getMateria());
        System.out.println(s1.getMatricola());
        System.out.println(s2.getMedia());
        System.out.println(s2.getEta());
        System.out.println(p1.getNome());
        System.out.println(p1.getCognome());

        p1.setMateria("Informatica");
        p1.setSalario(2000);
        s2.setEta(20);
        s2.setMedia(9.5);


        System.out.println(p1.getSalario());
        System.out.println(s2.getMatricola());
        System.out.println(s2.getMedia());
        System.out.println(p1.getNome());
        System.out.println(p1.getCognome());
        System.out.println(p1.getSalario());
        System.out.println(p1.getEta());
        System.out.println(p1.getMateria());
        System.out.println(s1.getEta());

        System.out.println(s1.toString());
        System.out.println(s2.toString());
        System.out.println(p1.toString());
    }
}
