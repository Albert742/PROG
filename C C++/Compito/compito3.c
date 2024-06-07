/*
!3-Unione tra array 
!Scrivi un programma in C che prenda due aray di interi inseriti dall'utente e cre un terzo array che contaga tutti gli elementi dei primi due array senza duplicati.
*/
#include <stdio.h>

int main() {
    int dim = 0, dim2 = 0, dim3 = 0, ar1[dim], ar2[dim2], ar3[dim3];
    printf(" Iserici la lunghezza del primo array: ");
    scanf ("%d", &dim);
    printf("Inserisci i valori del primo array: ");
    for (int i = 0; i < dim; i++){

        scanf ("%d", &ar1[i]);
    }

    printf(" Iserici la lunghezza del secondo array: ");
    scanf ("%d", &dim2);
    printf("Inserisci i valori del secondo array: ");
    for (int i = 0; i < dim; i++){

        scanf ("%d", &ar2[i]);
    }
    dim3 = dim + dim2;
    for (int i = 0; i < dim; i++){
        ar3[i] = ar1[i];
    }
    for (int i = 0; i < dim2; i++){
        int temp, temp2;
        temp = ar3[i];
        temp2 = ar2[i+1];
        if (temp != temp2){
        ar3[i + dim] = ar2[i];
        }
    }
    printf("I valori del terzo array sono: ");
    for (int i = 0; i < dim3; i++){

        printf("%d ", ar3[i]);
    }
}