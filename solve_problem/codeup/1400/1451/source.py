n = int(input())
number_list = []

for i in range(0, n):
    number = int(input())
    number_list.append(number)

number_list.sort()
for number in number_list:
    print(number)
