#!/bin/python3

import os
import sys


def pageCount(n, p):
    fromFront = p / 2
    fromBack = 0
    if(n % 2):
        fromBack = (n - p) / 2
    else:
        fromBack = (n - p + 1) / 2
    return min(int(fromFront), int(fromBack))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
