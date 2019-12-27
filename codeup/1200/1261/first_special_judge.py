
numbers = list(map(int, input().split()))
isQuintuple = False

for number in numbers:
    if(number % 5 == 0):
        print(number)
        isQuintuple = True
        break

if(isQuintuple == False):
    print('0')
