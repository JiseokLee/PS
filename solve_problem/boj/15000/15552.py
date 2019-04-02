import sys

n = int(sys.stdin.readline())
result = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    result.append(a+b)

for i in range(len(result)):
    print(result[i])
