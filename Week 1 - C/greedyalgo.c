#include <cs50.h> /*ensures that the user inputs an floateger */
#include <stdio.h>
#include <math.h>


/*
Step 1: prompt user for an amount of change
Step 2: always use the largest coin possible
Step 3: keep track of coins used
Step 4: print the final numbers of coins
https://stackoverflow.com/questions/25795266/greedy-algorithm-in-c
*/

int main(void)
{
    // declared my variables
    float amount;
    int cents = 0;
    int count = 0;
    int amount_left = 0;

    // prompt to user to input amount of change
    do
    {
        printf("O hai! How much change is owed?\n");
        amount = get_float(); // get amount as a float
        cents = (int)round(amount*100.0); // convert to cents and round it off to avoid floating point imprecision
        amount_left = cents;
    }
    while (amount < 0);

    while (amount_left >= 25) {
        count++;
        amount_left -= 25;
    }
    while (amount_left >= 10) {
        count++;
        amount_left -= 10;
    }
    while (amount_left >= 5) {
        count++;
        amount_left -= 5;
    }
    while (amount_left >= 1) {
        count++;
        amount_left -= 1;
    }
    printf("%d\n", count);
}



