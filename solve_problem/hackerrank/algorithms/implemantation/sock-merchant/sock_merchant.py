#!/bin/python3

import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
    socks = {}
    countPair = 0
    for color in ar:
        try:
            socks[color] += 1
        except:
            socks[color] = 1
    for color in socks:
        countPair += int(socks[color] / 2)
    return countPair


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
