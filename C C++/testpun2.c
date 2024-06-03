#include <stdio.h>

void swap(int *apt, int *bpt);

int main()
{
    int alfa = 5, beta = 13;
    printf("\nalfa -> %d, beta -> %d", alfa, beta);

    swap(&alfa, &beta);

    printf("\nalfa -> %d, beta -> %d", alfa, beta);
}

void swap(int *apt, int *bpt)
{
    int temp;
    temp = *apt;
    *apt = *bpt;
    *bpt = temp;  
}