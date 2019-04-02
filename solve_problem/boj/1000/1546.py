n = int(input())
score = list(map(int, input().split()))
highest_score = max(score)
result = 0

for scr in score:
    result += scr / highest_score * 100

print(result / n)
