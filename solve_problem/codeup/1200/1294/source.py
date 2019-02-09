text = input()
password = ''

for i in range(0, len(text)):
    if text[i] == ' ':
        password += text[i]
    elif ord(text[i]) > 119:
        if text[i] == 'x':
            password += 'a'
        elif text[i] == 'y':
            password += 'b'
        elif text[i] == 'z':
            password += 'c'
    else:
        code = ord(text[i]) + 3
        password += chr(code)

print(password)
