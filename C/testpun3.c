#include <stdio.h>

int* swap(int *apt, int *bpt);

int main()
{
    int alfa = 9, beta = 3;
    int *pointer;
    printf("\nalfa -> %d, beta -> %d", alfa, beta);

    pointer = swap(&alfa, &beta);

    printf("\n*pointer %d", *pointer);
}

int* swap(int *apt, int *bpt)
{
    int temp;
    temp = *apt;
    *apt = *bpt;
    *bpt = temp;  
    return bpt;
}