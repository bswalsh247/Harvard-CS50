# But there’s no way to get the pointers in Python, so the only way we can swap values is this:

x = 1
y = 2

print("x is {}".format(x))
print("y is {}".format(y))
print("Swapping...")
x, y = y, x # tuples
# you could do:
# tmp = x
# x = y
# y = temp   # but this is that elegant
print("Swapped.")
print("x is {}".format(x))
print("y is {}".format(y))


# In Python, we can actually swap variables with one line. The left side 
# and right side, x, y, and y, x are both tuples, a data structure with 
# multiple values, and we’re setting the items inside x, y to what the items 
# inside y, x are, which swaps the values.

# A function, too, can return multiple values, so we might need to 
# save them with something like a, b, c, d = foo()

