n = int(input())
numOfGroupWord = 0

for i in range(0, n):
    isGroupWord = True
    word = input()

    for c in word:
        if c * word.count(c) not in word:
            isGroupWord = False

    if isGroupWord:
        numOfGroupWord += 1

print(numOfGroupWord)
