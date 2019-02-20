h, r = map(int, input().split())


def zigzag(h):
    for i in range(0, h):
        for j in range(0, i):
            print(' ', end='')
        print('*')
    for i in range(h-2, -1, -1):
        for j in range(0, i):
            print(' ', end='')
        print('*')


for i in range(0, r):
    zigzag(h)
