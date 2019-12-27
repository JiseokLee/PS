
num = input()
num = int(num)
ordinal_num = ''

if(num % 10 == 1):
    ordinal_num = str(num) + 'st'
    if(num == 11):
        ordinal_num = str(num) + 'th'
elif(num % 10 == 2):
    ordinal_num = str(num) + 'nd'
    if(num == 12):
        ordinal_num = str(num) + 'th'
elif(num % 10 == 3):
    ordinal_num = str(num) + 'rd'
    if(num == 13):
        ordinal_num = str(num) + 'th'
else:
    ordinal_num = str(num) + 'th'

print(ordinal_num)
