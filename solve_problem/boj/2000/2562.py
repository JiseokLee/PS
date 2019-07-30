biggest = 0
index = 0

for i in range(9):
    num = int(input())
    if biggest < num:
        biggest = num
        index = i + 1

print(biggest)
print(index)
