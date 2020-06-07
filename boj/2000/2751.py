# 런타임 에러
# array = []
# number = int(input())

# def quickSort(data, start, end):
#     if start >= end:
#         return
    
#     pivot = start
#     i = start + 1
#     j = end
#     temp = 0

#     while(i <= j):
#         while i <= end and data[i] <= data[pivot]:
#             i += 1
#         while j > start and data[j] >= data[pivot]:
#             j -= 1
        
#         if i > j:
#             temp = data[j]
#             data[j] = data[pivot]
#             data[pivot] = temp
#         else:
#             temp = data[i]
#             data[i] = data[j]
#             data[j] = temp

#     quickSort(data, start, j - 1)
#     quickSort(data, j + 1, end)
        
# for i in range(number):
#     inputNum = int(input())
#     array.append(inputNum)

# quickSort(array, 0, number - 1)

# for num in array:
#     print(num)

n = int(input())
array = [int(input()) for _ in range(n)]

for num in sorted(array):
    print(num)