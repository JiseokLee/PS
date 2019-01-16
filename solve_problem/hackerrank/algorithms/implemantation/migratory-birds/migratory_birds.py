#!/bin/python3

import math
import os
import random
import re
import sys


def migratoryBirds(arr):
    count = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0}
    for num in arr:
        if(num == 1):
            count['1'] += 1
        elif(num == 2):
            count['2'] += 1
        elif(num == 3):
            count['3'] += 1
        elif(num == 4):
            count['4'] += 1
        elif(num == 5):
            count['5'] += 1
    maxNum = max(count, key=count.get)
    return maxNum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
