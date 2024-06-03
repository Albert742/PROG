/*
!Scrivere una funzione con prototipo void max_second_max (int a[], int n, int *max, int *second_max) che,
!dato un array a di lunghezza n individui il valore più grande in a e il secondo elemento per grandezza in a,
!e li memorizzi nelle variabili puntate da max e second_max.
*/

#include <stdio.h>

#define N 5

void F_max_secondmax(int a[], int n, int *max, int *secondmax);

int main()
{

    int a[N], n = N, i = 0, max, secondmax;
    printf("Inserisci %d valori\n", N);
    for (i = 0; i < n; i++)
    {
        printf("inserisci elemento di posto %d, valore:", i + 1);
        scanf("%d", &a[i]);
    }

    F_max_secondmax(a, n, &max, &secondmax);
    printf("\nmax: %d", max);
    printf("\nsecondmax: %d\n", secondmax);
}

void F_max_secondmax(int a[], int n, int *max, int *secondmax)
{
    int i;
    *max = a[0];
    *secondmax = 0;
    for (i = 0; i < n; i++)
    {
        printf("elemento di posto %d, valore %d\n", i + 1, a[i]);
        if (a[i] > *max)
        {
            *secondmax = *max;
            *max = a[i];
        }
        else if (a[i] > *secondmax)
        {
            *secondmax = a[i];
        }
    }
}