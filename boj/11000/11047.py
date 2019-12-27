n, k = map(int, input().split())
a = []
cnt = 0

for i in range(n):
    a.append(int(input()))
a.reverse()

for money in a:
    if(money <= k):
        while(money <= k):
            k -= money
            cnt += 1
    if(k == 0):
        break

print(cnt)