#!/bin/python3

from fractions import gcd
import os
import sys


def getTotalX(a, b):
    lcm_a = int(getLcmByArr(a))
    gcd_b = int(getGcdByArr(b))
    count = 0
    for i in range(lcm_a, gcd_b+1, lcm_a):
        if(gcd_b % i == 0):
            count += 1
    return count


def lcm(a, b):
    return a * b / gcd(a, b)


def getGcdByArr(arr):
    outputGcd = arr[0]
    for i in range(1, len(arr)):
        outputGcd = gcd(outputGcd, arr[i])
    return outputGcd


def getLcmByArr(arr):
    outputLcm = arr[0]
    for i in range(1, len(arr)):
        outputLcm = lcm(outputLcm, arr[i])
    return outputLcm


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    total = getTotalX(a, b)
    f.write(str(total) + '\n')
    f.close()
