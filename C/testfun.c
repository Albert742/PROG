#include<stdio.h>
#define N 5

void F_stampa_n(int a[N]) {
  for (int i = 0; i < N; i++) {
    printf("Stampato: %d\n", a[i]);
  }
}

int main() {
  int a[N], i, tot;
  for (i = 0; i < N; i++)
    {

        do 
        {

            printf("inserisci elemento %d: ", i + 1);

            scanf("%d", &a[i] );

        } while(a[i] <= 0);

    }
  F_stampa_n(a);
}

