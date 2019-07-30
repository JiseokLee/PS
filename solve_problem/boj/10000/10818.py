n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
print(numbers[0], numbers[len(numbers)-1])
