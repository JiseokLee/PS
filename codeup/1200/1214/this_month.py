
year, month = input().split()
year = int(year)
month = int(month)
february = 0

if(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
    february = 29
else:
    february = 28

if(month < 8):
    if(month == 2):
        print(february)
    elif(month % 2 == 0):
        print('30')
    else:
        print('31')
else:
    if(month % 2 == 0):
        print('31')
    else:
        print('30')
