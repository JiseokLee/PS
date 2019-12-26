n = int(input())
time = list(map(int, input().split()))
totalTime = 0
cumulativeTime = 0

time.sort()

for t in time:
    cumulativeTime += t
    totalTime += cumulativeTime

print(totalTime)