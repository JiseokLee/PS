import math

a, b, v = map(int, input().split())

if(v == a):
    day = 1
else:
    day = int(math.ceil((v-a) / (a-b)) + 1)

print(day)