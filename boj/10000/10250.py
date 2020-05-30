t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    
    if(n % h):
        room = (n % h * 100) + (int(n / h) + 1)
    else:
        room = (h * 100) + int(n / h)

    print(room)