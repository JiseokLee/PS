a, b, c, n = input().split()
a = int(a)
b = int(b)
c = int(c)
n = int(n)
number = a

for i in range(0, n-1):
    number = number * b + c

print(number)
