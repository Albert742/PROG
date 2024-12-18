#include<stdio.h>

int main(void) {
    int grade,i;

    printf("inserisci un numero: ");
    scanf("%d", &i);

    while (i > 0) {
        printf("T minus %d and counting\n", i);
        i--;
    }

}