/*
! 1-calcolo della somma dei primi N numeri
!Scrivi un programmain C che , dato un numero intero inserito dall'utente,calcoli la somma da 1 fino al N
*/

#include <stdio.h>

int main()
{
    int N = 0, i = 0, somma = 0;
    printf("Inserisci un numero: ");
    scanf("%d", &N);
    for (i = 1; i <= N; i++)
    {
        somma = somma + i;
    }
    printf ("la somma da 1 al N e': %d", somma);
}
