import collections

n = int(input())
numbers = list(map(int, input().split()))
numbers = collections.deque(numbers)
numbers.rotate(1)

for i in range(0, n):
    numbers.rotate(-1)
    for number in numbers:
        print(number, end=' ')
    print()
