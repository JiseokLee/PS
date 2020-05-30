n = input()
number = []
ans = ''

for item in n:
    number.append(item)

number.sort(reverse=True)

for item in number:
    ans += item
ans = int(ans)

if ans % 10 == 0 and ans % 3 == 0:
    print(ans)
else:
    print(-1)
