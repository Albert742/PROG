#include<stdio.h>

int main(void) {
    int i;

    for (i = 100; i > 0; i= i - 5)
        printf("T minus %d and counting\n", i);
}