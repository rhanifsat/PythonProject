def UbahHuruf(teks, a, b):
    lst = []
    lst[:0] = teks
    i = 0
    for x in lst:
        if x == a:
            lst[i] = b
        i += 1
    print(''.join(lst))

UbahHuruf('MATEMATIKA', 'T', 'S')