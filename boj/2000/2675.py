t = int(input())

for i in range(t):
    r, string = input().split()
    r = int(r)

    for ch in string:
        for j in range(r):
            print(ch, end='')

    print()
