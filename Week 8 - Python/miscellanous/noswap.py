# We can swap variables, without having to dereference pointers. If we try to pass them in:

def main():
    x = 1
    y = 2

    print("x is {}".format(x))
    print("y is {}".format(y))
    print("Swapping...")
    swap(x, y)
    print("Swapped.")
    print("x is {}".format(x))
    print("y is {}".format(y))

def swap(a, b):
    tmp = a
    a = b
    b = tmp

if __name__ == "__main__":
    main()


# The variables don’t get swapped, since they are being passed in as copies again. 
# a and b get swapped, but there is no permenant effect on the callers variables 
# in main's stack frame b/c that is fundamentally flawed 

#C 
# at those addresses.

#include <stdio.h>

void swap(int a, int b);

int main(void)
{
    int x = 1;
    int y = 2;

    printf("x is %i\n", x);
    printf("y is %i\n", y);
    printf("Swapping...\n");
    swap(x, y);
    printf("Swapped.\n");
    printf("x is %i\n", x);
    printf("y is %i\n", y);
}

void swap(int a, int b)
{
    int tmp = a;
    a = b;
    b = tmp;
}

# We have a function called swap that’s supposed to take two values, 
# a and b, and swaps them. It takes a, puts the value into a temporary variable 
# called tmp, and then stores the value of b into a. Then the value of tmp, which 
# is the original a, is stored into b.

# But when we run this program, too, it doesn’t swap the values of x and y in main.

# C using pointers 

# We can also fix our swap:

#include <stdio.h>

void swap(int *a, int *b);

int main(void)
{
    int x = 1;
    int y = 2;

    printf("x is %i\n", x);
    printf("y is %i\n", y);
    printf("Swapping...\n");
    swap(&x, &y);
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

# Now we’re passing in pointers to our main function’s x and y, and swapping 
# their values directly. The syntax to get an address of variable is with &, and to
# go the other way and get the value at some address is with a *. (Not to be confused
# with declaring a pointer, which would be using char * or int * to say 
# "I would like a new variable that stores a pointer to a char or int.")


# david's explanation:
# so we fundamentally fixed that with the version below by passing these variable in my reference
# by their addresss(aka pointers) and then we had to use the star operator inside swap 
# to deference those pointers those addresses and go to them to and actually change or get the values
# at those addresses.