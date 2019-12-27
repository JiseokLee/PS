s = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s_input = input()

for alpha in s:
    if alpha in s_input:
        s_input = s_input.replace(alpha, ' ')

print(len(s_input))
