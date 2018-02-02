#include <cs50.h> /*ensures that the user inputs an integer */
#include <stdio.h>

/*
Step 1: prompt and validate user input
Step 2: calculate equivalent bottles
Step 3: print equivalent bottles
*/

int main(void)
{
    int n; /* declared outside do-while scope */
    do
    {
        printf("Minutes: ");
        n = get_int(); /* store value of minutes inputted */
        n*=12;
        printf("Bottles: %i\n", n); /* %i is placeholder for int and n is variable to be printed */
    }
    while (n < 0);
}



