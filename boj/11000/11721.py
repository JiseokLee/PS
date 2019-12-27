word = input()

for i in range(0, int(len(word)/10)+1):
    print(word[i*10:i*10+10])
