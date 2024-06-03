#include<stdio.h>
#include<string.h>

int main(void){
    char str[100];
    printf("Inserisci una stringa: ");
    fgets(str, 100, stdin);
    printf("Ecco la stringa inserita:  \n\n%s", &str);
}