n = int(input())
conf = []

for i in range(n):
    conf.append(list(map(int, input().split())))
conf.sort(key=lambda x : [x[1],x[0]])

cnt = 1
j = 0

for i in range(1, len(conf)):
    if(conf[i][0] >= conf[j][1]):
        cnt += 1
        j = i

print(cnt)