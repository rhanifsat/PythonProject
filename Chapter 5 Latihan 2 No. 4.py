kolom = 5
baris = 5

i = 0
kolom -= kolom
while (i < baris):
    j = 0
    kolom += 1
    while (j < kolom):
        print('* ', end='')
        j += 1
    print('')
    i += 1