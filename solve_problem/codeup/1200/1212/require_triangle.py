
numbers = list(map(int, input().split()))
numbers.sort()

if(numbers[0] + numbers[1] > numbers[2]):
    print('yes')
else:
    print('no')
