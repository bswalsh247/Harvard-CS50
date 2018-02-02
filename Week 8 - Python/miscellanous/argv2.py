# And we can print each character in each argument:

import sys

for s in sys.argv:
    for c in s:
        print(c)
    print()

# With for s in sys.argv, we are accessing element in sys.argv, 
# and calling it s. And the type of each element will be a string.

# Then with for c in s, we are accessing each element in the string s, 
# which we will call c, since each element is a character.


# Let’s do this in C, to see how we can iterate over an array:

#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    for (int i = 0; i < argc; i++)
    {
        printf("%s\n", argv[i]);
    }
}

# This program prints out each argument, or each string in argv, 
# as it goes through the indexes from 0 to argc, which tells us how 
# many strings are in argv.

# We can be even cooler. Since we know argv is an array of strings and 
# each string is an array of characters, we can directly access characters from argv:

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    // iterate over strings in argv
    for (int i = 0; i < argc; i++)
    {
        // iterate over characters in current string
        for (int j = 0, n = strlen(argv[i]); j < n; j++)
        {
            // print j'th character in i'th string
            printf("%c\n", argv[i][j]);
        }
        printf("\n");
    }
}

# The outer for loop, with i, is iterating over each string in argv.

# The inner for loop, with j, looks at argv[i], and for each character in it, 
# prints it on a new line.

# Then the inner loop repeats for the next string.

# With argv[i][j] we can get an individual character in argv.





