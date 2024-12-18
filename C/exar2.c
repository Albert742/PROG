#include <stdio.h>
#include <stdbool.h>
#define N 5

int F_CRE(int a[], int lenght);
int F_DECR(int a[], int lenght);

int main()
{
    int a[N], i;
    int UsR;
    printf("Enter %d numbers.\n", N);
    for (i = 0; i < N; i++)
    {
        printf("inserisci elemento %d: ", i + 1);

        scanf("%d", &a[i]);
    }
    do
    {
        printf("\nCosa vuoi fare: ");
        printf("\n1 - Stampa ordine crescente");
        printf("\n2 - Stampa ordine decrescente");
        printf("\n3 - Esci");
        printf("\n Seleziona una funzione: ");
        scanf("%d", &UsR);
        switch (UsR)
        {
        case 1:
            F_CRE(a, N);
            break;

        case 2:
            F_DECR(a, N);
            break;

        case 3:
            printf("\nUscita...");
            break;

        default:
            printf("\nSelezione incorretta.");
            break;
        }

    } while (UsR != 3);
}

int F_CRE(int a[], int lenght)
{
    int i, j;
    for (i = 0; i <= lenght; i++)
    {
        for (j = i + 1; j < lenght; j++)
        {
            if (a[i] > a[j])
            {
                int temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
    }
    printf("Ordine crescente: ");
    for (i = 0; i < lenght; i++)
    {
        printf("%d ", a[i]);
    }
}

int F_DECR(int a[], int lenght)
{
    int i, j;
    for (i = 0; i < lenght; i++)
    {
        bool Scambiato = false;
        for (j = i + 1; j < lenght; j++)
        {
            if (a[i] < a[j])
            {
                int temp = a[i];
                a[i] = a[j];
                a[j] = temp;
                Scambiato = true;
            }
            if (!Scambiato)
            {
                break;
            }
        }
    }
    printf("Ordine decrescente: ");
    for (i = 0; i < lenght; i++)
    {
        printf("%d ", a[i]);
    }
}
