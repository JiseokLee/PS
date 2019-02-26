string = input()
openBracket = 0
closeBracket = 0

for i in range(0, len(string)):
    if string[i] == '(':
        openBracket += 1
    elif string[i] == ')':
        closeBracket += 1

print(openBracket, closeBracket)
