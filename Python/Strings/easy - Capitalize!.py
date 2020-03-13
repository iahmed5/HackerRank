#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    names = s.split(" ")
    capitalString = ""
    for name in names:
        capitalString += name[0:1].upper() + name[1:len(name)].lower() + " "

    return capitalString[0:len(capitalString) - 1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
