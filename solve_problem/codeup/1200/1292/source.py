dna = input()
dnaSum = 0

for i in range(0, 10):
    dnaSum += int(dna[i])

if dnaSum % 7 == 4:
    print('suspect')
else:
    print('citizen')
