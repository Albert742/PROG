#include <stdio.h>
int main(void)
{
    int alfa = 4, beta = 7;
    int *pointer;
    pointer = &alfa;
    printf("\n-\nalfa -> %d, beta -> %d, pointer -> %p", alfa, beta, pointer);
    beta = *pointer;
    printf("\n-\nalfa -> %d, beta -> %d, pointer -> %p", alfa, beta, pointer);
    alfa = pointer;
    printf("\n-\nalfa -> %p, beta -> %d, pointer -> %p", alfa, beta, pointer);
    *pointer = 5;
    printf("\n-\nalfa -> %d, beta -> %d, pointer -> %p", alfa, beta, pointer);
}