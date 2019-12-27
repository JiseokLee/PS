n = int(input())
numbers = list(map(int, input().split()))

print(numbers[0], end=' ')
print(numbers[int(n/2)], end=' ')
print(numbers[n-1], end=' ')
