#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Implement a program that, given a person’s name, prints a person’s initials, per the below.

int main(void)
{
    // get person's name
    string s = get_string();
    if (s != NULL)
    {
        // print the first character in name and make it uppercase. requires <ctype.h>
        printf("%c", toupper(s[0]));

        // loop through the full name
        for ( int i = 0, n = strlen(s); i < n; i++) // better design to store strlen function in variable n.
        {
            // check space and end of characters
            if ( s[i] == ' ')
            {
                // print the rest of the initials w/ uppercase character and increment
                printf("%c", toupper(s[i + 1]));
            }
        }
    }
    printf("\n");
}