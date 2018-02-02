# We can write a familiar program that uses various operators in python:

import cs50

# prompt user for x
print("x is ", end="")
x = cs50.get_int()

# prompt user for y
print("y is ", end="")
y = cs50.get_int()

# perform calculations for user
print("{} plus {} is {}".format(x, y, x + y))
print("{} minus {} is {}".format(x, y, x - y))
print("{} times {} is {}".format(x, y, x * y))
print("{} divided by {} is {}".format(x, y, x / y))
print("{} divided by {} (and floored) is {}".format(x, y, x // y))
print("remainder of {} divided by {} is {}".format(x, y, x % y))

# There is a special operator in Python, //, that divides two integers 
# and returns an integer that’s truncated (with everything after the decimal point removed).

# And comments in Python, instead of starting with //, will start with #.

# And we pass in end="" as an additional argument to print if we don’t want 
# a new line to be added for us automatically at the end.

# If you wanted to write the this same thing in C it would look like:
int main(void){	
}
	printf("x is ");
	int x = get_int();

	# // prompt user for y
	printf("y is ");
	int y = get_int();

	# // perform calculations for user
	printf("%i plus %i is %i\n", x, y, x + y);
	printf("%i minus %i is %i\n", x, y, x - y);
	printf("%i times %i is %i\n", x, y, x * y);
	printf("%i divided by %i is %i\n", x, y, x / y);
	printf("remainder of %i divided by %i is %i\n", x, y, x % y);
}