#include <cs50.h> /*ensures that the user inputs an integer */
#include <stdio.h>

/*
Step 1: prompt and validate user input
Step 2: draw the half pyramid
*/

int main(void)
{
    // my variables
    int height; /* declared outside do-while scope */
    int row;
    int space;
    int hash;

    // prompt to user to input height of pyramid between 0 and 23
    do
    {
        printf("Height: ");
        height = get_int(); // store value of height inputted
    }
    while (height < 0 || height > 23);

    // loop to create number of rows based on user input
    for (row = 1; row <= height; row++) // if the row is less than or equal to height then start another row
    {
        for (space = height - row; space > 0; space--) // loop to print spaces
        {
            printf(" ");
        }
        for (hash = 0; hash < row + 1; hash++) // loop to print hashes
        {
            printf("#");
        }

        printf("\n");
    }
}



