numbers = list(map(int, input().split()))
biggest_even = 0
biggest_odd = 0

for number in numbers:
    if (number % 2 == 0) and (number > biggest_even):
        biggest_even = number
    elif (number % 2 == 1) and (number > biggest_odd):
        biggest_odd = number

if biggest_even == 0:
    print(biggest_odd)
elif biggest_odd == 0:
    print(biggest_even)
else:
    print(biggest_odd, biggest_even)
