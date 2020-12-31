print('------------------------------------')
print('|Selamat Datang di Program Enkripsi|')
print('------------------------------------')
direktori = input('Masukkan direktori file yang akan dienkripsi: ')
geser = int(input('Berapa kali akan digeser tiap hurufnya: '))
myfile = open(direktori, 'r')
teks = myfile.read()
sandi = []
for huruf in teks:
    kode = int(ord(huruf)) + geser
    sandi.append(chr(kode))
for kode in sandi:
    enkripsi = open('d:\TeksSandi.txt', 'a')
    enkripsi.write(kode)