# We can add logic in python, too:

import cs50

c = cs50.get_char()
if c == "Y" or c == "y":
    print("yes")
elif c == "N" or c == "n":
    print("no")
else:
    print("error")

# We get a char, and compare it to Y or y or N or n to tell us if we said yes or no.

# We just say or and and in Python instead of || and &&.

# And in C, we needed to compare chars by using single quotes, but in Python single 
# characters are also strings. The good news is, we can compare strings with a 
# simple == and it will compare them the way we might expect, equalling True if the 
# strings have the same contents. Even more mind-blowingly, in Python single quotes 
# ' and double quotes " can both be used to indicate strings, as long as we use the same one on both sides of the string.

# In C, it looks like this:

# include <cs50.h>
#include <stdio.h>

int main(void)
{
	int c = get_char();
	if (c == 'Y' || c == 'y')
	{
		printf("yes\n");
	}

	else if (c == 'N' || c == 'n')
	{
		printf("no\n");
	}
	else
	{
		printf("error\n");
	}
}
