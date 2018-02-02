# recall this program in C, when we executed the code below, we got this result:

#include <stdio.h>

int main(void)
{
	printf("%.55f\n", 1.0 / 10.0);
}

#result
`0.1000000000000000055511151231257827021181583404541015625`


# We can print floating-point numbers with enough decimal places to see 
# imprecision in Python, too:

print("{:.55f}".format(1 / 10))

# The value we want to print is 1 / 10, and to specify the format we 
# place :55f inside the curly braces of the string.

# And if we run that, we see:

`0.1000000000000000055511151231257827021181583404541015625`

# However, if we don't want to see floating point imprecision then you simply write:

print("{}".format(1/10))

#result
0.1