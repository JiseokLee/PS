n = int(input())
numbers = list(map(int, input().split()))
count_even = 0

for number in numbers:
    if number % 2 == 0:
        count_even += 1

print(count_even)
