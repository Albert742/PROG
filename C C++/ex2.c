#include<stdio.h>
#include<string.h>

int main(void) {
    char Nome[100];
    int Tpag;
    float Prezzo;
    printf("Inserici il nome del prodotto: ");
    scanf("%s", &Nome[100]);
    printf("Inserisci il prezzo del prodotto:");
    scanf("%f", &Prezzo);
    printf("Inserisci tipo di pagamento Contanti(1) o Carta(2)?");
    scanf("%d", &Tpag);

    if (Prezzo > 3000) {
        printf("\nPrezzo di 3000 Eur superato applicato sconto del 6/100");
        Prezzo = Prezzo - 0.06 * Prezzo;
    } 
    if (Tpag == 1) {
        printf("\nTipo di pagamento usato Contanti applicato sconto del 2/100");
        Prezzo = Prezzo - 0.02 * Prezzo;
     }
    printf("\nPrezzo finale: %.2f", Prezzo);
}