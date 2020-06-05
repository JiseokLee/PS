n = int(input())

if n != 1:
    for i in range(n - 1):
        print(' ', end='')
    print('*')

for i in range(n - 2):
    for _ in range(n - 2 - i):
        print(' ', end='')
    print('*', end='')
    for _ in range(i * 2 + 1):
        print(' ', end='')
    print('*')

for i in range(n * 2 - 1):
    print('*', end='')
print()