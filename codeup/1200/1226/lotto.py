
winNumbers = list(map(int, input().split()))
inputNumbers = list(map(int, input().split()))
numberOfMatch = 0
isBonusMatch = False
bonusNumber = winNumbers[6]
del winNumbers[6]

winNumbers.sort()
inputNumbers.sort()

for winNumber in winNumbers:
    for inputNumber in inputNumbers:
        if(winNumber == inputNumber):
            numberOfMatch += 1

if(numberOfMatch == 6):
    print('1')
elif(numberOfMatch == 5):
    for inputNumber in inputNumbers:
        if(inputNumber == bonusNumber):
            isBonusMatch = True
            break
        else:
            isBonusMatch = False
    if(isBonusMatch == True):
        print('2')
    else:
        print('3')
elif(numberOfMatch == 4):
    print('4')
elif(numberOfMatch == 3):
    print('5')
else:
    print('0')
