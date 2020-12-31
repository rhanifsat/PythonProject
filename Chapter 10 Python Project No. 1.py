myfile = open('d:\data.txt', 'w')
myfile.write('100\n')
myfile.write('102\n')
myfile.write('99\n')
myfile.write('89\n')
myfile.write('192\n')
myfile.write('938\n')
myfile.write('107\n')
myfile.write('241\n')
myfile.close()

myfile = open('d:\data.txt', 'r')
teks = myfile.readlines()
i = 0
ganjil = 0
genap = 0
for x in teks:
    if int(teks[i]) % 2 == 0:
        genap = genap + 1
    else:
        ganjil= ganjil + 1
    i += 1
print('Banyaknya bilangan genap :', genap)
print('Banyaknya bilangan ganjil:', ganjil)
myfile.close()