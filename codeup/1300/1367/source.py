n = int(input())

for i in range(n-1, -1, -1):
    for j in range(0, i):
        print(' ', end='')
    for j in range(0, n):
        print('*', end='')
    print()
