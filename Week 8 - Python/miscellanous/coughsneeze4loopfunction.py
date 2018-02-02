# And we can add multiple arguments to a function:

def main(): # defining or own main function that calls two functions that are paramaterized each of which in turn call some other functions like def cough that take multiple parameters so we are already building up those building blocks even faster then we woudl have done in the earlier weeks of the class. 
    cough(3)
    sneeze(3)

def cough(n):
    say("cough", n)

def sneeze(n):
    say("achoo", n)

def say(word, n):
    for i in range(n):
        print(word)

if __name__ == "__main__":
    main()

# Since we’re only printing the word variable that’s 
# passed into our say function, we can just say print(word).

# in C:

#include <stdio.h>
#include <cs50.h>

void cough(int n);
void say(string word, int n);
void sneeze(int n);

int main(void)
{
	cough(3); 
    sneeze(3);
}

void cough(int n)
{
	for (int i = 0; i < n; i++)
	{
		printf("cough\n")
	}
}

# in C: