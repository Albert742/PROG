#include <stdio.h>

#define N 100

void F_max_secondmax(int a[], int n, int *max, int *secondmax);

int main()
{
    int a[N], n = 0, i = 0, max, secondmax;
    printf("quanti valori vuoi considerare (max %d)? ", N);
    scanf("%d", &n);

    for (i = 0; i < n; i++)
    {
        printf("\ninserisci elemento di posto %d, valore:\n", i + 1);
        scanf("%d", &a[i]);
    }

    F_max_secondmax(a, n, &max, &secondmax);
    printf("max: %d\n", max);
    printf("secondmax: %d\n", secondmax);
}

void F_max_secondmax(int a[], int n, int *max, int *secondmax)
{
    if (n < N)
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
}