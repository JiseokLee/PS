n = int(input())
hash_record = {}

for i in range(0, n):
    name, score = input().split()
    hash_record[name] = int(score)

data = sorted(hash_record.items(), key=lambda t: t[1], reverse=True)
print(data[2][0])
