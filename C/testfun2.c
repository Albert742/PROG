#include<stdio.h>
#include<stdbool.h>

bool n_primo(int n) {
    int divisore;
    if (n <= 1)
        return false;
    for (divisore = 2; divisore * divisore; divisore++)
        if (n % divisore == 0)
            return false;
    return true;
}

int main (void) {
    int n;

    printf("inserisci un numero: ");
    scanf("%d", &n);
    if (n_primo(n))
        printf("primo\n");
    else
        printf("non primo");
    return 0;
}