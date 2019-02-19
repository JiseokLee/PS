h, k, d = input().split()
h, k = int(h), int(k)

if d == 'L':
    for i in range(0, h):
        for j in range(0, i):
            print(' ', end='')
        for j in range(0, k):
            print('*', end='')
        print()
else:
    for i in range(h-1, -1, -1):
        for j in range(0, i):
            print(' ', end='')
        for j in range(0, k):
            print('*', end='')
        print()
