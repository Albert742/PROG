#include<stdio.h>

int main(void) 
{
    int A,B;
    printf("Inserisci A: ");
    scanf("%d",&A);

    printf("Inserisci B: ");
    scanf("%d",&B);

    if (A > B) {
        printf("A maggiore di B \nA= %d", A);
        } else {
        printf("B maggiore di A \nB= %d", B);
        }
 }