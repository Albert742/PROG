import java.util.Scanner;

public class test2 {
    public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    System.out.println("Inserisci il tuo voto: ");
    int voto = 0;
    do {
    voto = input.nextInt();
        if (voto < 0 || voto > 10) {
            System.out.println("Il voto deve essere compreso tra 0 e 10");
        }
    } while (voto < 0 || voto > 10);
    input.close();
        if (voto >= 6) {
            System.out.println("Sei passato");
        } else {
            System.out.println("Sei bocciato");
        }
    }
}
