#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    // throws an error if user doesn't provide a command-line argument or provides more than one command-line argument
    if (argc != 2)
    {
        printf("Missing command-line argument or have too many\n");
        return 1;
    }
    else
    {
        // Convert the string to an integer
        int k = atoi(argv[1]);

        // prompt user to enter plaintext
        printf("plaintext: ");
        string p = get_string();

        printf("ciphertext: ");
        // make sure get_string returned a string
        if (p != NULL)
        {
            // iterate over the characters in p one at a time
            for (int i = 0, n = strlen(p); i < n; i++)
            {
                // if alphabetic
                if (isalpha(p[i]))
                {
                    // preserve case and apply equation to lower case characters
                    if (islower(p[i]))
                    {
                        printf("%c", ((((p[i] - 97) + k) % 26) + 97));
                    }
                    // preserve case and apply equation to uppercase characters
                    else
                    {
                        printf("%c", ((((p[i] - 65 ) + k) % 26) + 65));
                    }
                }
                // print out non-alphabetic characters unchanged
                else
                {
                    printf("%c", p[i]);
                }
            }
            printf("\n");
            return 0;
        }
    }
}
