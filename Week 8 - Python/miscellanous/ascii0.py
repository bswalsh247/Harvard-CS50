# Let’s see if we can convert characters to ASCII:

for i in range(65, 65 + 26):
    print("{} is {}".format(chr(i), i))

# We can specify the starting number and the ending number 
# in a range (including the starting number but not the ending number).

# Then we print chr(i) first, and then i, using the chr() function 
# in Python to convert an integer into a char.

# In C, there’s another feature called typecasting that lets you convert one 
# type of data to another. Characters are stored in memory as binary numbers, 
# so we can convert them back and forth.

# Remember that ASCII is a standard for mapping characters to letters. Here are 
# some sample ones:

# A   B   C   D   E   F   G   H   I  ...
# 65  66  67  68  69  70  71  72  73  ...

# a   b   c   d   e   f   g   h   i   ...
# 97  98  99  100 101 102 103 104 105 ...

# We can experiment with this program:

#include <stdio.h>

int main(void)
{
    for (int i = 65; i < 65 + 26; i++)
    {
        printf("%c is %i\n", (char) i, i);
    }
}

# We print out i as a character by typecasting it, using (char) i to tell our 
# program to treat i as a character.