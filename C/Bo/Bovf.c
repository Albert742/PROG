#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void print_haha() {
    printf("haha\n");
}


int main(int argc, char *argv[]) {
    char buffer[5];
    if (argc < 2){
        printf("strcpy() NOT EXEC...\n");
        printf("Syntax: %s <characters>\n", argv[0]);
        exit(0);
    }
    strcpy(buffer, argv[1]);
    printf("buffer content= %s\n", buffer);
    // you may want to try strcpy_s()
    printf("strcpy() EXEC...\n");
    return 0;
}