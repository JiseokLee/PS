array = []
index = 0
number = int(input())

for i in range(0, number):
    array.append(int(input()))

for i in range(0, number):
    minNum = 1001
    for j in range(i, number):
        if minNum > array[j]:
            minNum = array[j]
            index = j
    temp = array[i]
    array[i] = array[index]
    array[index] = temp

for num in array:
    print(num)