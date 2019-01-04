#!/bin/python3

import math
import os
import random
import re
import sys


def plusMinus(arr):
    numOfElement = len(arr)
    numOfPlus = 0
    numOfMinus = 0
    numOfZero = 0

    for number in arr:
        if(number < 0):
            numOfMinus += 1
        elif(number > 0):
            numOfPlus += 1
        else:
            numOfZero += 1

    print(round(numOfPlus / numOfElement, 6))
    print(round(numOfMinus / numOfElement, 6))
    print(round(numOfZero / numOfElement, 6))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
