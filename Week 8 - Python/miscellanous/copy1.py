# To copy a string, we can do this:

import cs50
import sys

print("s: ", end="")
s = cs50.get_string()

if s == None:
    exit(1)

t = s.capitalize()

print("s: {}".format(s))
print("t: {}".format(t))

exit(0)


# Now we can run the program and see that t has a capitalized version of s, 
# while s itself is unchanged.

# Recall that s is an object in Python, so it has built-in functions that we 
# can call from that object with the . syntax, so we can use s.capitalize() 
# that automatically takes the first character and capitalizes it.

# Furthermore, strings in Python are immutable, meaning that they can’t be 
# changed after they have been created. So s.capitalize() returns a copy of 
# s that has been capitalized, which we then need to store somewhere. (Though, 
# technically, we could store that right back into s with s = s.capitalize(), 
# but it would be a "new" string.)

#C
# Let’s try to copy the string:

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    printf("s: ");
    string s = get_string();
    if (s == NULL)
    {
        return 1;
    }

    string t = s;

    if (strlen(t) > 0)
    {
        t[0] = toupper(t[0]);
    }

    printf("s: %s\n", s);
    printf("t: %s\n", t);

    return 0;
}

# Now we’re getting a string s from the user, copying it to a string called t,
#  and then making the first letter of t uppercase.

# But when we run the program, it again doesn’t behave like we might expect. Both s 
# and t are capitalized!

# C using pointers

# To make a copy of a string, we do something a little fancier:

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    printf("s: ");
    char *s = get_string();
    if (s == NULL)
    {
        return 1;
    }

    char *t = malloc((strlen(s) + 1) * sizeof(char));
    if (t == NULL)
    {
        return 1;
    }

    for (int i = 0, n = strlen(s); i <= n; i++)
    {
        t[i] = s[i];
    }

    if (strlen(t) > 0)
    {
        t[0] = toupper(t[0]);
    }

    printf("s: %s\n", s);
    printf("t: %s\n", t);

    free(t);

    return 0;
}

# We get s as usual, but then for t we use another C library function called malloc, 
# which allocates some memory for us to use. The amount of memory we ask for is the 
# length of s (plus 1 for \0 to end the string), times the size of a single character. 
# And if malloc returns NULL for t, that means something went wrong (perhaps we ran 
# out of memory), so our program too needs to check for that and return an error if so.

# Now we can deliberately go through the entire string, and one past the end of the string, 
# to copy the \0 character. Then we’ll have a copy of s in t, and changing something in t 
# will no longer change s.

# Finally, at the end of our program, we should make the habit of calling free on our 
# manually allocated memory, which marks it as usable again.



