
day1, day2, day3 = input().split()
day1 = int(day1)
day2 = int(day2)
day3 = int(day3)
day = 1

while(day%day1 != 0 or day%day2 != 0 or day%day3 != 0):
    day += 1

print(day)