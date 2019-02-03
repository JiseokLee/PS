import math

n = int(input())
a = []
index = 0
sq = int(math.sqrt(float(n)))

for i in range(0, 30):
    a.append(0)

for i in range(2, sq+1):
    while n % i == 0:
        n /= i
        a[index] = i
        index += 1

if n != 1:
    a[index] = n
    index += 1
if index == 2:
    print(int(a[0]), int(a[1]))
else:
    print('wrong number')
