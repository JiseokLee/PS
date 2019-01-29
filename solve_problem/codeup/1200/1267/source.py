length = int(input())
numbers = list(map(int, input().split()))
result = 0

for number in numbers:
    if number % 5 == 0:
        result += number

print(result)
