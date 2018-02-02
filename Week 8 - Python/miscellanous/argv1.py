# We can print all of the arguments we get:

import sys

for i in range(len(sys.argv)): #len(sys.argv) is the same as argc in C.
    print(sys.argv[i])

