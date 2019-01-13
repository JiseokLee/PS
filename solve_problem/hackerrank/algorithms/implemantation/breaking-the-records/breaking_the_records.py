#!/bin/python3

import math
import os
import random
import re
import sys


def breakingRecords(scores):
    countBestScore = 0
    countWorstScore = 0
    bestScore = scores[0]
    worstScore = scores[0]
    for score in scores:
        if(bestScore < score):
            countBestScore += 1
            bestScore = score
        elif(worstScore > score):
            countWorstScore += 1
            worstScore = score
    return countBestScore, countWorstScore


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
