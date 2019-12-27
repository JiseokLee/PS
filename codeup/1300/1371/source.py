n = int(input())

for i in range(0, n):
    for j in range(n-i-1, 0, -1):
        print(' ', end='')
    print('*', end='')
    for j in range(0, i*2):
        print(' ', end='')
    print('*')

for i in range(0, n):
    for j in range(0, i):
        print(' ', end='')
    print('*', end='')
    for j in range((n-i-1)*2, 0, -1):
        print(' ', end='')
    print('*')
