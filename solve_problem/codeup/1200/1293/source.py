n = int(input())
scores = list(map(int, input().split()))
highest = scores[0]
lowest = scores[0]

for score in scores:
    if score > highest:
        highest = score
    if score < lowest:
        lowest = score

print(highest, lowest)
