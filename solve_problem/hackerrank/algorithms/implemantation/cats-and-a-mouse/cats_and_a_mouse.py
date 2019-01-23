#!/bin/python3

import math
import os
import random
import re
import sys


def catAndMouse(x, y, z):
    catA = x - z
    catB = y - z
    output = ''

    if(catA < 0):
        catA = catA * -1
    if(catB < 0):
        catB = catB * -1

    if(catA == catB):
        output = 'Mouse C'
    elif(catA > catB):
        output = 'Cat B'
    elif(catA < catB):
        output = 'Cat A'

    return output


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
