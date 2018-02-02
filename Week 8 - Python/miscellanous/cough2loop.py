# And we can create a function:

def main():
    for i in range(3):
        cough()

def cough():
    print("cough")

if __name__ == "__main__":
    main()

# We can add an argument to our cough function:

def main():
    cough(3)

def cough(n):
    for i in range(n):
        print("cough")

if __name__ == "__main__":
    main()

# Here cough takes in some argument n, which the language sets to an int automatically for us.

# In C:

#include <stdio.h>

void cough(void);
{
	for (int i = 0; i < 3; i++)
	{
		cough();
	}
}

void cough(void)
{
	printf("cough\n");
}

