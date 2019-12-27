#!/bin/python3

import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    arr.sort()
    everySum = 0

    for number in arr:
        everySum += number

    miniSum = everySum - arr[4]
    maxSum = everySum - arr[0]

    print(miniSum, maxSum)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
