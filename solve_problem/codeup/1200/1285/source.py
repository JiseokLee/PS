expression = input()
result = 0
symbol = ''
lastNumber = 0
lsatSymbol = ''
lastIndex = 0
isFirst = True

for i in range(0, len(expression)):
    if expression[i] in ('+', '-', '*', '/', '='):
        symbol = expression[i]
        number = int(expression[lastIndex:i])
        lastIndex = i+1

        if isFirst:
            isFirst = False
            result += int(number)
            lastNumber = number
            lsatSymbol = symbol
            continue

        if lsatSymbol == '+':
            result += number
            result = int(result)
        elif lsatSymbol == '-':
            result -= number
            result = int(result)
        elif lsatSymbol == '*':
            result *= number
            result = int(result)
        elif lsatSymbol == '/':
            result /= number
            result = int(result)

        lsatSymbol = symbol

print(int(result))
