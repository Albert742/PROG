/*
!Scrivere una funzione con prototipo int* point_min (int a[], int a_size) che, dato un array di lunghezza a_size,
!restituisca un puntatore all'elemento più piccolo dell'array
*/
#include <stdio.h>
#define a_size 5

int *p_min(int a[], int size);
void Fin_array(int a[]);


int main()
{
    int a[a_size];

    Fin_array(a);

    int *pMinn = p_min(a, a_size);

    printf("\nValore numerico minimo:  %d\n \nIndirizzo del valore in array:  %p", *pMinn, pMinn);
}

void Fin_array(int a[])
{
    for (int i = 0; i < a_size; i++)
    {
        printf("\nInserisci elemento %d valore: ", i + 1);
        scanf("%d", &a[i]);
    }
}

int *p_min(int a[], int size)
{
    int min_inx = 0;
    for(int i = 1; i < a_size; i++)
    {
        if (a[min_inx] > a[i])
        {
            min_inx = i;
        }
    }
    printf("\nPosizione del minimo nell'array a[%d] \nInput numero: %d\n", min_inx, min_inx + 1);
    return &a[min_inx];
}