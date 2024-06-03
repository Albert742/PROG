import java.util.Scanner;

class test {
    public static void main(String[] args) {
        System.out.println("Numeri statici");
        int stnum1 = 210;
        int stnum2 = 42;
        System.out.println(stnum1);
        System.out.println(stnum2);
        System.out.println("\nSomma stnum1 e stnum2: " + (stnum1 + stnum2));
        System.out.println("\nDifferenza stnum1 e stnum2: " + (stnum1 - stnum2));
        System.out.println("\nMoltiplicazione stnum1 e stnum2: " + (stnum1 * stnum2));
        System.out.println("\nDivisione stnum1 e stnum2: " + ((double)stnum1 / stnum2));
        
        Scanner input = new Scanner(System.in);
        System.out.println("\nScrivi un numero: ");
        int num1 = input.nextInt();
        System.out.println("\nIl primo numero che hai scritto e': " + num1);
        System.out.println("\nScrivi un altro numero: ");
        int num2 = input.nextInt();
        input.close();
        System.out.println("\nIl secondo numero che hai scritto e': " + num2);
        System.out.println("\nSomma num1 e num2: " + (num1 + num2));
        System.out.println("\nDifferenza num1 e num2: " + (num1 - num2));
        System.out.println("\nMoltiplicazione num1 e num2: " + (num1 * num2));
        System.out.println("\nDivisione num1 e num2: " + ((double)num1 / num2));
        
    }
}