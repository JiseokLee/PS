n, m = map(int, input().split())

for i in range(n, 0, -1):
    for j in range(0, m):
        print(i*m-j, end=' ')
    print()
