n = int(input())
room = 1
distance = 1

while room < n:
    room += distance * 6
    distance += 1

print(distance)
