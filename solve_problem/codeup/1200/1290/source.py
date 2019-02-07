n = int(input())
countPiece = 0

for i in range(1, n):
    if n % i == 0:
        countPiece += 1

print(countPiece)
