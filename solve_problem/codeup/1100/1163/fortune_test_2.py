
year, month, day = input().split()
year = int(year)
month = int(month)
day = int(day)

num = (year + month + day) % 1000
num = num / 100

if(num % 2 == 0):
    print('대박')
else:
    print('그럭저럭')
