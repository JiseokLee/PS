
year, month, day = input().split()
year = int(year)
month = int(month)
day = int(day)

if((year-month+day) % 10 == 0):
    print('대박')
else:
    print('그럭저럭')
