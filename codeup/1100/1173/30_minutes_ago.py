
hour, minute = input().split()
hour = int(hour)
minute = int(minute)

if(minute - 30 < 0):
    minute = 60 + (minute - 30)
    if(hour - 1 < 0):
        hour = 23
    else:
        hour -= 1
else:
    minute -= 30

print(str(hour) + ' ' + str(minute))
