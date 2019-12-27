n = int(input())
matrix = [[0]*n for i in range(n)]
row, col = map(int, input().split())


def abs(num):
    return num if num > 0 else -num


def get_number(a, b):
    return abs(a-(row-1)) + abs(b-(col-1)) + 1


for i in range(0, n):
    for j in range(0, n):
        print(get_number(i, j), end=' ')
    print()
