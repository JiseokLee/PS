index = 0
array = list(map(int, input().split()))

for i in range(0, 3):
    minNum = 1000001
    for j in range(i, 3):
        if minNum > array[j]:
            minNum = array[j]
            index = j
    temp = array[i]
    array[i] = array[index]
    array[index] = temp

for num in array:
    print(num, end=' ')
print()