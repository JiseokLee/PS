#!/bin/python3

import math
import os
import random
import re
import sys


def countApplesAndOranges(s, t, a, b, apples, oranges):
    appleCount = 0
    orangeCount = 0
    fellPointApple = list(map(lambda apple: apple + a, apples))
    fellPointOrange = list(map(lambda orange: orange + b, oranges))

    for point in fellPointApple:
        if(s <= point <= t):
            appleCount += 1

    for point in fellPointOrange:
        if(s <= point <= t):
            orangeCount += 1

    print(appleCount)
    print(orangeCount)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
