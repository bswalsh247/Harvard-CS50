// http://valgrind.org/docs/manual/quick-start.html#quick-start.prepare.

#include <stdlib.h>

void f(void)
{
	// request to malloc for enough space for 10 integers. 
	// A size of an int is 4 bytes or 32 bits. So this is asking for 40 bytes.
	// malloc returns the address of that chunk of memory and stores it in x which is the address of an int.
    int *x = malloc(10 * sizeof(int));
    // the code below is bad because 10 is an index. An index starts at 0 and we only asked for 10 bytes not 11 bytes.
    // additionally we aren't freeing the memory after this.
    x[9] = 0;
    free(x);
}

int main(void)
{
    f();
    return 0;
}