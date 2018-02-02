#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // get line of text
    char *s = get_string();
    if (s == NULL)
    {
        return 1;
    }

    // print string, one character per line
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        // same as printf("%c\n", s[i]; this version is called syntactic sugar b/c the syntax is nice to have b/c its' more convient or easier to read. 
        // The version below tho arcane looking is perhaps more well defined syntax and express of what is actually happening underneath the hood
        // *s is the address of the first char in the string inputed by the user.
        // value i is equal to 0 defined in the for loop. So s + 0 is just s
        // so this print function is saying go print the first character of this string
        // and on the second iteration of the loop i=1 so s + 1 is one byte farther from the beginning of the string
        // and * means go to that character address + 1 to get the second character. Repeat until loop has completed length of string.
        printf("%c\n", *(s+i)); 
    }
}

