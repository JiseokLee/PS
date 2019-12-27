word = input().upper()
counts = [0] * 27

for i in range(0, 26):
    counts[i] = word.count(chr(i+65))

mostCount = max(counts)

if counts.count(mostCount) >= 2:
    print('?')
else:
    print(chr(counts.index(mostCount)+65))
