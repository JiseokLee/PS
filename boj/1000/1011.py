import math

t = int(input())

for i in range(t):
    start, end = map(int, input().split())
    dist = end - start
    k = 1
    
    while(k*k <= dist):
        k += 1
    if(k*k != dist):
        k -= 1
    dist = math.ceil((dist - k*k) / k)

    print(int(k * 2 - 1 + dist))