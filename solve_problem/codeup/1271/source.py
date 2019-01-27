n = input()
numbers = list(map(int, input().split()))
maximum_number = 0

for number in numbers:
    if(number > maximum_number):
        maximum_number = number

print(maximum_number)
