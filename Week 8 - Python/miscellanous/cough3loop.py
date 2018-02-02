# And we can add multiple arguments to a function:

def main():
    cough(3)

def cough(n):
    for i in range(n):
        print("cough")

if __name__ == "__main__":
    main()

# Since we’re only printing the word variable that’s 
# passed into our say function, we can just say print(word).

# in C:

#include <stdio.h>

void cough(int n);

int main(void)
{
	cough(3); # here we paramaterized cough so we could cough 3 times but not have to implement the loop ouselves in main
}

void cough(int n)
{
	for (int i = 0; i < n; i++)
	{
		printf("cough\n")
	}
}

# in C: