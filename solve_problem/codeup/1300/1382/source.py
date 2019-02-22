for i in range(1, 10):
    for j in range(2, 6):
        print('%d x %d = %2d' % (j, i, j*i), end='')
        print('\t', end='')
    print()
