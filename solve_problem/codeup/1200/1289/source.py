largest = 0

for i in range(0, 3):
    h, v = map(int, input().split())
    if largest < (h * v):
        largest = h * v

print(largest)
