
def d(n):
    return n + sum(map(int, list(str(n))))


self_number = {}

for i in range(1, 10001):
    if i not in self_number:
        print(i)
    self_number[d(i)] = 1
