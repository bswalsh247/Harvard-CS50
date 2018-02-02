# We can also exit with some value, much like returning some exit code in C:

import cs50
import sys

if len(sys.argv) != 2:
    print("missing command-line argument")
    exit(1)

print("hello, {}".format(sys.argv[1]))
exit(0)

# In Python, to end a program, since there might not always be a main function 
# to return from, we call exit with some value.

# And recall that in the command line, we can type echo $? to see the return 
# value of the last program that ran.

# C
# So what about main's output? It turns out, main also returns some value by default. 
# When a program exits successfully, it returns a number 0 to indicate as much. 
# A non-zero number, on the other hand, is used to represent an error.

# Of course, we want to see this firsthand:

#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("missing command-line argument\n");
        return 1;
    }
    printf("hello, %s\n", argv[1]);
    return 0;
}

# Now, if the program doesn’t get a command-line argument, the program will quit 
# by returning, and with the value 1.

# Otherwise, we’ll print the argument and explicitly return the value 0 as we exit.

# We can see the exit code in terminal like this:

# ~/workspace/ $ ./exit
# missing command-line argument
# ~/workspace/ $ echo $?
# 1
# $? is a magic symbol for the previous program’s exit code, and echo is a 
# command-line program that just prints out values.

# We might not look for this often, but debuggers and other programs might
# look for it to determine if there were any errors.


