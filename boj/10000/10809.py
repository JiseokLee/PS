word = input()

for asc in range(ord('a'), ord('z')+1):
    if chr(asc) not in word:
        print(-1, end=' ')
        continue
    else:
        for i in range(0, len(word)):
            if word[i] == chr(asc):
                print(i, end=' ')
                break
