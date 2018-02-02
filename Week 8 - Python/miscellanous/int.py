# in C we would write:

#include <cs50.h>
#include <stdio.h>

int main(void)
{
	int i = get_int();
	printf("hello, %i\n", i);
}

# Similarly in python, we can get a number:

import cs50

i = cs50.get_int()
print("hello, {}".format(i))