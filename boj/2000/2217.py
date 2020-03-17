n = int(input())
ans = 0
rope_list = []

for i in range(n):
    rope_list.append(int(input()))
rope_list.sort()

for i in range(0, len(rope_list)):
    ans = max(ans, rope_list[i]*(n-i))

print(ans)