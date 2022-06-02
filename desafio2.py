#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    string = s
    number = n
    a_count = 0

    if len(string) <= number:
        for letter in string:
            if 'a' in letter:
                a_count += 1

        a_count *= (((a_count*100)/len(string))/100)

        a_count_aux = 0
        for letter in string[:number-len(string)]:
            if 'a' in letter:
                a_count_aux += 1
        a_count += a_count_aux
    
    else:
        for letter in s[:n]:
            if 'a' in letter:
                a_count += 1
            
    return a_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()