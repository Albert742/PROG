/*dato un array di N (definita come constante) elementi, 
chiedere all'utente di inserire da tastiera dei numeri.
Una volta che l'array è popolato:
-trovare il più grande
-trovare il più piccolo
-sommare tutti
-stampare i dispari
-stampare i pari
-chiedere un numero e verificare se e quante volte è presente
-fare reinserire i valori <=0 */

#include<stdio.h>
#define N 5

int main(void){

int a[N], i, tot = 0, U, c = 0, maxn = 0, minn;

char R;

    printf("Inserisci %d numeri. \n", N);

    for (i = 0; i < N; i++)
    {

        do 
        {

            printf("inserisci elemento %d: ", i + 1);

            scanf("%d", &a[i] );

        } while(a[i] <= 0);

    }

    for (i = 0; i < N; i++)
    {

        tot = a[i]+tot;

        if (a[i] >= maxn)    
        {

            maxn = a[i];
            minn = a[0];

        } else if (a[i] <= minn)
        {

            minn = a[i];

        }
            
            switch (a[i])
            {
            case 0:

                printf("\nNumero neutro: %d", a[i]);

                break;

            default:

                if(a[i]%2 == 0)
                {

                    printf("\nTrovato il numero pari: %d", a[i]);

                } else 
                {

                    printf("\nTrovato il numero dispari: %d", a[i]);

                }

            }

    }

    printf("\nIl totale e': %d", tot);

    printf("\nil numero massimo e': %d", maxn);

    printf("\nil numero minimo e': %d \n", minn);

    printf("\nVuoi cercare un numero? (S/N)");

    scanf(" %c", &R);

        if (R == 'S' || R == 's')
        {

            printf("\ninserisci il numero da cercare nell'array: ");

            scanf("%d", &U);

            for (i = 0; i < N; i++)
            {

                if (a[i] == U)
                {

                    c++;

                }

            }

        } else 
        {

            return 0;

        }

        if (c > 0)
        {

            printf("\nVerificata presenza del numero nell'array");

            printf("\nIl numero e' presente %d volte", c);

        } else 
        {

            printf("\nIl numero non e' presente nell'array");

        }
}