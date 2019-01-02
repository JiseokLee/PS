#!/bin/python3

import math
import os
import random
import re
import sys


def compareTriplets(a, b):
    alicePoint = 0
    bobPoint = 0
    for i in range(0, 3):
        if(a[i] > b[i]):
            alicePoint += 1
        elif(a[i] < b[i]):
            bobPoint += 1
    return alicePoint, bobPoint


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
