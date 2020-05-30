a, b = input().split()
ans = 51
cnt = 0

for i in range(0, len(b) - len(a) + 1):
    cnt = 0
    for j in range(0, len(a)):
        if a[j] != b[j+i]:
            cnt += 1
    ans = min(cnt, ans)

print(ans)