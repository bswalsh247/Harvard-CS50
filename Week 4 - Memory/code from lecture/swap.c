#include <stdio.h>

void swap(int *a, int *b);

int main(void)
{
    int x = 1;
    int y = 2;

    printf("x is %i\n", x);
    printf("y is %i\n", y);
    printf("Swapping...\n");
    swap(&x, &y); // & means get me the address of x and y variables and pass those in. If it was just x and y then it would be a copy that would be past in
    printf("Swapped!\n");
    printf("x is %i\n", x);
    printf("y is %i\n", y);
}

void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}