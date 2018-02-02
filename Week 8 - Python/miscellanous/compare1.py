# We can compare two strings:

import cs50
import sys

print("s: ", end="")
s = cs50.get_string()

print("t: ", end="")
t = cs50.get_string()

if s != None and t != None:
    if s == t: # in C, this would not have worked b/c it would have been comparing two pointers (aka two memory addresses). In C, we use strcmp function
        print("same")
    else:
        print("different")


# Instead of null, since we don’t need to worry about pointers as much anymore, 
# there is a special value that get_string might return, None, that indicates 
# there is nothing returned.

# In C, s and t would be two addresses that would not be the same, but in Python 
# the contents of s and t would be compared automatically for us.

# Let’s look at compare0.c:

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    printf("s: ");
    string s = get_string();

    printf("t: ");
    string t = get_string();

    if (s == t)
    {
        printf("same\n");
    }
    else
    {
        printf("different\n");
    }
}

# It looks like this program takes two strings from the user and compares them.

# But it doesn’t work, when we put in two strings that look the same.

# C using pointers

# So how might we compare a string?

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    printf("s: ");
    char *s = get_string();

    printf("t: ");
    char *t = get_string();

    if (s != NULL && t != NULL)
    {
        if (strcmp(s, t) == 0)
        {
            printf("same\n");
        }
        else
        {
            printf("different\n");
        }
    }
}
# Now that we know what get_string actually returns, we can set the type of our 
# variable s to char *, or a pointer to a character. (And indeed the CS50 Library 
# 	has just been mapping all mentions of string to char * this whole time!)

# Turns out, there exists a library function called strcmp that compares strings, and 
# returns 0 if they’re the same. And strcmp probably does that with a loop looking at 
# the ith character in each string, comparing them one at a time.


