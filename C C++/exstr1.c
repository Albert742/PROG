/*
!calcolare la lunghezza
!uguaglianza tra stringhe
!concatenare stringhe
!invertire ordine stringa
!copiare una stringa in un'altra
!creare e popolare vettore da 10 stringhe, acquisire stringa, ricercarla in vettore contare le ripetizioni con intero
*/

#include <stdio.h>
#define N 2
#define D 100

void F_instr(char str[]);
void F_prstr(char str[]);
int F_lenstr(char str[]);
void F_compstr(char str[]);
void F_unstr(char str[]);
void F_invstr(char str[]);
void F_copstr(char str[]);
void F_srcstr(char strv[][D]);

int main()
{
    char str[D], strv[N][D];
    int UsR;
    do
    {
        printf("\nCosa vuoi fare: ");
        printf("\n0 - Inserisci stringhe");
        printf("\n1 - Stampa stringhe");
        printf("\n2 - Calcola lunghezza stringhe");
        printf("\n3 - Compara lunghezza stringhe");
        printf("\n4 - Concatena stringhe");
        printf("\n5 - Inverti stringhe");
        printf("\n6 - Copia stringa in un'altra");
        printf("\n7 - Ricerca stringhe uguali");
        printf("\n8 - Esci");
        printf("\n Seleziona una funzione: ");
        scanf("%d", &UsR);
        switch (UsR)
        {
        case 0:
            F_instr(str);
            break;

        case 1:
            F_prstr(str);
            break;

        case 2:
            int len = F_lenstr(str);
            printf("\nLunghezza stringa: %d", len);
            break;

        case 3:
            F_compstr(str);
            break;

        case 4:
            F_srcstr(str);
            break;

        case 5:
            F_srcstr(str);
            break;

        case 6:
            F_srcstr(str);
            break;

        case 7:
            F_srcstr(strv);
            break;

        case 8:
            printf("\nUscita...");
            break;

        default:
            printf("\nSelezione incorretta.");
            break;
        }

    } while (UsR != 8);
}

void F_instr(char str[D])
{
    printf("\nInserisci stringa: ");
    scanf("%s", str);
}

void F_prstr(char str[D])
{
    printf("\nStringa %d inserita: %s\n", &str);
}

int F_lenstr(char str[D])
{
    int i = - 1;
    do 
    {
        i++;
    } while (str[i] != '\0');
    return i;
}
void F_compstr(char str[D])
{


}

void F_unstr(char str[][D])
{
    int len1 = F_lenstr;
}
void F_invstr(char str[][D])
{
    int ;
    char ;
    int ;
}
void F_copstr(char str[][D])
{

}

void F_srcstr(char strv[][D])
{
    char stringa[D];
    int src = 0, i, cc = 0;
    for (i = 0; i < N; i++)
    {
        printf("\nInserisci stringa %d: ", i + 1);
        scanf("%s", strv[i]);
    }
    for (int i = 0; i < N; i++)
    {
        printf("\nStringa %d inserita: %s\n", i + 1, strv[i]);
    }
    printf("\nInserisci la stringa da cercare: ");
    scanf("%s", stringa);
    for (i = 0; i < N; i++)
    {
        int j = 0;
        while (strv[i][j] == stringa[j]) {
            if (strv[i][j] == '\0' || stringa[j] == '\0')
                break;
            j++;
        }
        if (strv[i][j] == '\0' && stringa[j] == '\0') {
            src = 1;
            cc++;
        }
    }
    if (src != 0)
    {
        printf("\nTrovata la stringa '%s'\n", stringa);
        printf("\nTrovata %d volte\n", cc);
    }
    else
    {
        printf("\nLa stringa '%s' non presente\n", stringa);
    }
}