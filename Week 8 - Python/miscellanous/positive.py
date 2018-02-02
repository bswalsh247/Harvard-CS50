# In C, we also once implemented a program to get a positive integer:

#include <cs50.h>
#include <stdio.h>

int get_positive_int(); # prototype

int main(void)
{
    int i = get_positive_int();
    printf("%i is a positive integer\n", i);
}

int get_positive_int(void)
{
    int n;
    do
    {
        printf("n is ");
        n = get_int();
    }
    while (n < 1);
    return n;
}

# We needed to first delare the function, then a variable n, and then a do while loop.

# Now we can write this in python:

import cs50

def main():
    i = get_positive_int()
    print("{} is a positive integer".format(i))

def get_positive_int():
    while True:
        print("n is ", end="")
        n = cs50.get_int()
        if n > 0:
            break
    return n

if __name__ == "__main__":
    main()


# We don’t need to declare get_positive_int before we call it, as long as it doesn’t 
# actually need to be run before we get to the part of the code that defines it. 
# In this case, we call get_positive_int in main, but main itself isn’t called until the 
# very last line, so everything in our program should already be defined.

# And we don’t need to specify that get_positive_int takes no arguments, so we can just 
# add a () instead of (void).

# Python also doesn’t have a do while loop, so instead we use while True, but break, or 
# stop the loop, if n > 0.

# Then it returns n, but notice that we also didn’t need to declare it outside the loop 
# before we used it. n will be created the first time our loop runs, and then have the new 
# value stored inside it every time after.

# And finally, we need to call the main function with the last two lines.

# here is another way of writing this in python. But you if stay with the version at the top
# b/c it's more like C which is what we want to stick with. 

def get_positive_int():
    while True:
        print("n is ", end="")
        n = cs50.get_int()
        if n > 0:
            break
    return n

i = get_positive_int()
print("{} is a positive integer".format(i))



