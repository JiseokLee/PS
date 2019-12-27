#!/bin/python3

import os
import sys


def gradingStudents(grades):
    for i in range(0, len(grades)):
        c = grades[i] % 5
        if(grades[i] > 37 and 5-c < 3 and c != 0):
            grades[i] = grades[i] + 5 - c
            if(grades[i] > 100):
                grades[i] = 100

    return grades


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
