numbers = []

for i in range(0, 5):
    number = input()
    numbers.append(int(number))

numbers.sort()

print(numbers[len(numbers) - 1])
print(numbers[0])
