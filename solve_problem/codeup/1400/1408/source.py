password = input()
encrypt_1 = ''
encrypt_2 = ''

for i in range(0, len(password)):
    asc = ord(password[i]) + 2
    encrypt_1 += chr(asc)
    asc = int((ord(password[i]) * 7) % 80 + 48)
    encrypt_2 += chr(asc)

print(encrypt_1)
print(encrypt_2)
