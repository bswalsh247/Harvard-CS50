# We could reimplement cough, to "cough" 3 times:

print("cough")
print("cough")
print("cough")

# in C:

#include <stdio.h>

int main(void)
{
	printf("cough\n");
	printf("cough\n");
	printf("cough\n");
}