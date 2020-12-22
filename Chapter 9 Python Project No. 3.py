def bintang(n):
    baris = n/2
    i = 0
    x = 1
    c = (n * 2) + 1
    while (i < baris - 1):
        star = '*' * x
        print(star.center(c), end='\n')
        x += 2
        i += 1
    baris = (n/2)
    i = n
    x = n
    c = (n * 2) + 1
    while (i > baris):
        star = '*' * x
        print(star.center(c), end='\n')
        x -= 2
        i -= 1

bintang(7)