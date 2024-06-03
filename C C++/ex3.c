#include<stdio.h>
/*indicare i primi 20 numeri dispari
per i primi 30 indicare quali dispari e quali pari
stampare numeri da -15 e +15 saltando 0,-10 e 10*/
int main(void){
    int N, Nc, c, d=0, p=0;
    char R, R1, R2;
    printf("Fino a che numero vuoi contare? ");
    scanf("%d", &N);
    printf("Da che numero si vuole cominciare? ");
    scanf("%d", &Nc);
    printf("Vuoi escludere i numeri '-15', '-10', '0', '10' e '15'? \n(S/N)\n");
    scanf(" %c", &R);
    printf("Vuoi stampare solo i numeri dispari? \n(S/N)\n");
    scanf(" %c", &R1);
    printf("Vuoi contare solo i numeri dispari? \n(S/N)\n");
    scanf(" %c", &R2);
        if (R1 == 'n' || R1 == 'N')
        {
            for (c = Nc; c <= N;c++)
            {

                if (R == 'S' || R == 's')
                {

                    switch (c)
                    {
                        case -15:
                            printf("\nEscluso");
                            break;
                        case -10:
                            printf("\nEscluso");
                            break;
                        case 0:
                            printf("\nEscluso");
                            break;
                        case 10:
                            printf("\nEscluso");
                            break;
                        case 15:
                            printf("\nEscluso");
                            break;
                        default:
                            if(c%2 == 0)
                            {
                                printf("\nTrovato il numero pari: %d", c);
                                p++;

                            } else 
                            {
                                printf("\nTrovato il numero dispari: %d", c);
                                d++;
                            }
                    }

                 } else if (R == 'N' || R == 'n') 
                 {
                    switch (c)
                    {
                    case 0:
                        printf("\nNumero neutro: %d", c);
                        break;
                    
                    default:
                    if(c%2 == 0)
                    {
                        printf("\nTrovato il numero pari: %d", c);
                        p++;
                    } else 
                    {
                        printf("\nTrovato il numero dispari: %d", c);
                        d++;
                    }
                    }

                } else {
                    printf("\nInput errato usa solo 'S'/'s' o 'N'/'n' nella prima domanda!");
                    break;
                }
            }
        } else if (R1 == 'S' || R1 == 's')
        {
            for (c = Nc; c <= N;c++)
            {

                if (R == 'S' || R == 's')
                {

                    switch (c)
                    {
                        case -15:
                            printf("\nEscluso");
                            break;
                        case -10:
                            printf("\nEscluso");
                            break;
                        case 0:
                            printf("\nEscluso");
                            break;
                        case 10:
                            printf("\nEscluso");
                            break;
                        case 15:
                            printf("\nEscluso");
                            break;
                        default:
                            if(c%2 !=0)
                            {
                                printf("\nTrovato il numero dispari: %d", c);
                                d++;
                            }
                     }

                } else if (R == 'N' || R == 'n') 
                {

                    if(c%2 !=0)
                    {
                        printf("\nTrovato il numero dispari: %d", c);
                        d++;
                    }

                } else 
                {
                    printf("\nInput errato usa solo 'S'/'s' o 'N'/'n' nella prima domanda!");
                    break;
                }
            }
        }

    if (R2 == 'S' || R2 == 's')
    {
        printf("\nIl totale di numeri dispari trovati e': %d", d);

    } else if (R2 == 'N' || R2 == 'n')
    {
        printf("\nIl totale di numeri dispari trovati e': %d", d);
        printf("\nIl totale di numeri pari trovati e': %d", p);

    } else 
    {
        printf("\nInput errato usa solo 'S'/'s' o 'N'/'n' nella terza domanda! \nContati pari e dispari per default");
        printf("\nIl totale di numeri dispari trovati e': %d", d);
        printf("\nIl totale di numeri pari trovati e': %d", p);
    }
}
