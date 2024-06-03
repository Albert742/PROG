/*
!Scrivere una funzione con prototipo int* point_min (int a[], int a_size) che, dato un array di lunghezza a_size,
!restituisca un puntatore all'elemento più piccolo dell'array
*/
#include <stdio.h>
#define a_size 5

int *p_min(int a[], int size);
void Fin_array(int a[]);
void Fp_addarray(int a[]);

int main()
{
    int a[a_size];
    int UsR;
    do
    {
        printf("\nCosa vuoi fare: ");
        printf("\n1 - Inserisci elementi ");
        printf("\n2 - Stampa array con indirizzi");
        printf("\n3 - Stampa elemento minimo array con indirizzo");
        printf("\n4 - Esci");
        printf("\n Seleziona una funzione: ");
        scanf("%d", &UsR);
        switch (UsR)
        {
        case 1:
            Fin_array(a);
            break;

        case 2:
            Fp_addarray(a);
            break;

        case 3:
            int *pMinn = p_min(a, a_size);

            printf("\nValore numerico minimo:  %d\n \nIndirizzo del valore in array:  %p\n", *pMinn, pMinn);
            break;

        case 4:
            printf("\nUscita...");
            break;

        default:
            printf("\nSelezione incorretta.");
            break;
        }

    } while (UsR != 4);
}

void Fin_array(int a[])
{
    for (int i = 0; i < a_size; i++)
    {
        printf("\nInserisci elemento %d valore: ", i + 1);
        scanf("%d", &a[i]);
    }
}

void Fp_addarray(int a[])
{
    for (int i = 0; i < a_size; i++)
    {
        printf("\nElemento %d, valore: %d, indirizzo: %p", i + 1, a[i], &a[i]);
    }
}

int *p_min(int a[], int size)
{
    int min_inx = 0;
    for (int i = 1; i < a_size; i++)
    {
        if (a[min_inx] > a[i])
        {
            min_inx = i;
        }
    }
    printf("\nPosizione del minimo nell'array a[%d] \nInput numero: %d\n", min_inx, min_inx + 1);
    return &a[min_inx];
}