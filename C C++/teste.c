#include<stdio.h>
 int main (void){
    int n[3];
for (int i = 0; i < 3; i++) {
  do {
    printf("Enter Number %d: ", i+1);
  } while (scanf("%d", n+i) >= 0);
}
 }