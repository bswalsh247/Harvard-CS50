# We can use command-line arguments too:

import sys

if len(sys.argv) == 2:
    print("hello, {}".format(sys.argv[1]))
else:
    print("hello, world")


# We can check the length of the arguments with len(sys.argv), and 
# access the second one (recall that the first is the program’s own name) 
# with sys.argv[1]. Here sys is a module built into Python that has command-line arguments
# and others.

# In C:

# Now our program will receive two arguments. The first is an integer named argc,
# as in argument count, that tells us how many arguments we got. The second is an array, 
# or list, of strings, called argv, as in argument vector. This list of strings can be 
# accessed with the same syntax as we do for characters in a string (since a string is 
# just an array of characters), like argv[0].

# Let’s see this in action:

#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        printf("hello, %s\n", argv[1]);
    }
    else
    {
        printf("hello, world\n");
    }
}

# This program, when we run it, will return something like the following 
# if we give it a command-line argument:

# ~/workspace/ $ ./argv0 hello
# hello, hello
# We used argv[1] because argv[0] is always the name of the program itself.

# When we run just ./argv0, argc passed to our program will be 1, so it will 
# just say hello, world.




