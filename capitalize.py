#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
# def solve(s):
#     a=s.split()
#     for i in a:
#         i.capitalize(a)
#         return(" ".join(a))  
    

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     result = solve(s)

#     fptr.write(result + '\n')

#     fptr.close()

s="hello priyanshu singh my name is"
x=s.split(' ')
print(x)
for i in x:
    print(i.capitalize())

print(" ".join(x))

