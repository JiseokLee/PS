
sum_of_num = 0
a, b = input().split()
a = int(a)
b = int(b)

for i in range(a, b+1):
    if(i % 3 == 0):
        sum_of_num += i

print(sum_of_num)
