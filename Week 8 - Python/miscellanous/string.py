// This is how we would write the hello world in C

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string name = get_string();
    printf("hello, %s\n", name);
}

// This is how we write hello world program in Python

import cs50

s = cs50.get_string()
print("hello, {}".format(s))

// The syntax for including a library is to use import.

// Then we declare a variable called s, and not need to specify the type, 
// and we call cs50.get_string() and store the return result into s.

// Then we include s in what we print. Strings, or more generally objects, 
// have built-in functions. We can call those functions with the syntax shown, 
// like "hello, {}".format(s), and by passing in the correct arguments, we can 
// substitute variables the way we want.

// Python also has an input function, which we can use instead of the CS50 library:

s = input("name: ")
print("hello, {}".format(s))

// We can pass in a prompt inside that function, and get the typed value back at the same time.

s = input("name: ")
print("hello, {}".format(s))

