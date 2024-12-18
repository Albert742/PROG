#include<stdio.h>
#define N 5

int main(void){
    int a[N], i;
    printf("Inserisci %d numeri. \n", N);
    for (i = 0; i < N; i++){
        printf("inseriscli il %d° elemento: ", i + 1);
        scanf("%d", &a[i]);
    }
    printf("\nOrdine inverso: ");
    for (i = N - 1; i >= 0; i--){
        printf("\n %d", a[i]);
    }
    return 0;
}