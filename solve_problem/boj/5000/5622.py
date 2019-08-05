s = '22233344455566677778889999'
input_s = input()
time = 0

for c in input_s:
    time += int(s[ord(c)-65]) + 1

print(time)
