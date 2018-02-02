// Now we’ll take a closer look at strings and how they are actually stored by the computer.

// It looks like this program takes two strings from the user and compares them.

// But it doesn’t work, when we put in two strings that look the same.

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

// Hm, mysterious. Let’s try to copy the string:

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
// Now we’re getting a string s from the user, copying it to a string called t, and then making the first letter of t uppercase.

// But when we run the program, it again doesn’t behave like we might expect. Both s and t are capitalized!

// Another example we can look at:

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