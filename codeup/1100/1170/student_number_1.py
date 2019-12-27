
grade, group, number = input().split()
number = int(number)

if(number < 10):
    number = '0' + str(number)

print(grade + group + str(number))
