size1, size2 = map(int, input().split())
array_1 = list(map(int, input().split()))
array_2 = list(map(int, input().split()))

result = array_1 + array_2
result.sort()

for item in result:
    print(item, end=' ')
