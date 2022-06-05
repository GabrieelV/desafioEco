#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    list_a_z = string.ascii_lowercase
    odd_count = 0
    for letter in list_a_z:
        if (s.count(letter) % 2) != 0:
            odd_count += 1
            
    if odd_count > 1:
        return 'NO'
    else:
        return 'YES'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
