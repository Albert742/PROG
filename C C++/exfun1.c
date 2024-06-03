#include <stdio.h>
#define N 5

void F_stampa(int a[], int lenght);
int F_stampaMa(int a[], int lenght);
int F_spampaMi(int a[], int lenght);
int F_stampaTo(int a[], int lenght);
void F_stampaDP(int a[], int lenght);
int F_trovaN(int a[], int U, int lenght);

int main()
{
   int a[N], i, tot = 0, U, c = 0;
   char UsR = 'a';
   printf("Enter %d numbers.\n", N);
   for (i = 0; i < N; i++)
   {

      do
      {

         printf("inserisci elemento %d: ", i + 1);

         scanf("%d", &a[i]);

      } while (a[i] <= 0);
   }
   do
   {
      printf("\nCosa vuoi fare: ");
      printf("\n1 - Stampa array");
      printf("\n2 - Max");
      printf("\n3 - Min");
      printf("\n4 - Totale");
      printf("\n5 - Stampa Pari/Dispari");
      printf("\n6 - Trova numero");
      printf("\n7 - Esci");
      printf("\n Seleziona una funzione: ");
      scanf("%d", &UsR);
      switch (UsR)
      {
      case 1:
         F_stampa(a, N);
         break;

      case 2:
         printf("\nMax: %d ", F_stampaMa(a, N));
         break;

      case 3:
         printf("\nMin: %d ", F_spampaMi(a, N));
         break;

      case 4:
         printf("\nTotale array: %d ", F_stampaTo(a, N));
         break;

      case 5:
         F_stampaDP(a, N);
         break;

      case 6:
         printf("\ninserisci il numero da cercare nell'array: ");

         scanf("%d", &U);
         c = F_trovaN(a, N, U);
         if (c > 0)
         {

            printf("\nVerificata presenza del numero nell'array");

            printf("\nIl numero e' presente %d volte", c);
         }
         else
         {

            printf("\nIl numero non e' presente nell'array");
         }
         break;
      case 7:
         printf("\nUscita...");
         break;
      default:
         printf("\nSelezione incorretta.");
         break;
      }

   } while (UsR != 7);
}

void F_stampa(int a[], int lenght)
{
   int i;
   printf("\nStampa numeri:\n");
   for (i = 0; i < lenght; i++)
   {
      printf("\n%d* Numero: %d ", i + 1, a[i]);
   }
}

int F_stampaMa(int a[], int lenght)
{
   int i, maxn = a[0];
   for (i = 1; i < lenght; i++)
   {
      if (a[i] > maxn)
         maxn = a[i];
   }
   return maxn;
}

int F_spampaMi(int a[], int lenght)
{
   int i, minn = a[0];
   for (i = 1; i < lenght; i++)
   {
      if (a[i] < minn)
         minn = a[i];
   }
   return minn;
}

int F_stampaTo(int a[], int lenght)
{
   int i, tot = 0;
   for (i = 0; i < lenght; i++)
      tot = tot + a[i];
   return tot;
}

void F_stampaDP(int a[], int lenght)
{
   int i;
   for (i = 0; i < lenght; i++)
   {
      if (a[i] % 2 == 0)
         printf("\nPari: %d ", a[i]);
      else
         printf("\nDispari: %d ", a[i]);
   }
}

int F_trovaN(int a[], int lenght, int U)
{
   int i, c = 0;
   for (i = 0; i < lenght; i++)
   {
      if (a[i] == U)
         c++;
   }
   return c;
}
