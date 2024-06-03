public class MainES1 {
    public static void main(String[] args) {
        PersonES1 p1 = new PersonES1("Tale", "Dei Tali", 19);
        PersonES1 p2 = new PersonES1("Tizio", "Ignoto", 18);
        PersonES1 p3 = new PersonES1("Mario", "Rossi", 19);

        System.out.println(p1.name);
        System.out.println(p2.getSurname());
        System.out.println(p3.age);
        
        //classe Person surname modificabile solo perché presente metodo set ma più privata  
        p2.setSurname("Rossi");
        System.out.println(p2.getSurname());

        //classe Person age modificabile direttamente perché pubblica 
        p3.age = 20;
        System.out.println(p3.age);
    }
}
