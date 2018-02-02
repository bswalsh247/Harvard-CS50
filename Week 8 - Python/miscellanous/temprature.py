# We can write a python program to convert temperature:

import cs50

f = cs50.get_float()
c = 5.0 / 9.0 * (f - 32.0)
print("{:.1f}".format(c))


# We first get a float, f, apply the correct formula and save the result to c, 
# and we want to format it to one decimal place so we use :1f.