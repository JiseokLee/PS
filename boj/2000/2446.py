n = int(input())

for i in range(n - 1):
    for _ in range(i):
        print(' ', end='')
    for _ in range((n * 2) - (i * 2) - 1):
        print('*', end='')
    print()

for i in range(n - 1):
    print(' ', end='')
print('*')

for i in range(n - 2, -1, -1):
    for _ in range(i):
        print(' ', end='')
    for _ in range((n * 2) - (i * 2) - 1):
        print('*', end='')
    print()