#!/bin/python3

import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    firstDiagonal = 0
    secondDiagonal = 0

    for i in range(0, len(arr)):
        firstDiagonal += arr[i][i]
    for i in range(0, len(arr)):
        secondDiagonal += arr[i][len(arr)-1-i]

    diagonalDifference = firstDiagonal - secondDiagonal
    if(diagonalDifference < 0):
        diagonalDifference = diagonalDifference * -1

    return diagonalDifference


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
