/*
!2-Nmero magico 
!Scrivi un programma in C che permetta all'utente di giocare al "Numero magico".Il proggramma deve generare un numero casuale tra 1 e 100, e l'utente deve indovinare il numero.Il programma deve fornire un menu con le seguenti opzioni:
!1-Inizia una nuova partita
!2-Visualizza il numero dei tentatativi dell'ultima partita
!3-Esci dal programma.
*/ 
#include<stdio.h>
#include<math.h>

int main() {
    int  Nc = 0, N = 0, t = 0, c = 0;
while (c != 3) {
    printf("\n1-Inizia una nuova partita\n2-Visualizza il numero dei tentatativi dell'ultima partita\n3-Esci dal programma\n");
    printf("Segli che oprazione vuoi fare: ");
    scanf("%d", &c);
    if (c < 1 || c > 3) {
        printf("\nInserimento errato");
        printf("\nRiprova: ");
        scanf("%d", &c);
    }
    switch (c) 
    {
        case 1 :
            Nc = rand() % 5 + 1;
            printf("\nInserisci un numero tra 1 e 100: ");
            scanf("%d", &N);
            t = 1;
            while (N != Nc) {
            if (N != Nc) {
                printf("\nNumero sbagliato");
                printf("\nRiprova: ");
                scanf("%d", &N);
                t++;
            }
            }
            printf("\nHai indovinato\n");
            break;
        case 2 :
            printf("\nHai tentato %d volte\n", t);
            break;
        case 3 :
            printf("\nUscita...");
            break;
        }
    }
}
