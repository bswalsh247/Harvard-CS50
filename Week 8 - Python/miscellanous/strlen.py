# In Week 2, we implemented strlen ourselves:

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = get_string();
    int n = 0;
    while (s[n] != '\0')
    {
        n++;
    }
    printf("%i\n", n);
}

# In Python, these implementation details are less and less visible, 
# so we’ll need to use documentation more frequently and rely more on 
# built-in functions that are already written for us:

import cs50

s = cs50.get_string()
print(len(s))