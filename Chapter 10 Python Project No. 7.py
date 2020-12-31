print('-----------------------------------------------')
print('|Selamat Datang di Program Terjemahan Enkripsi|')
print('-----------------------------------------------')
direktori = input('Masukkan direktori file: ')
geser = int(input('Berapa kali akan digeser tiap hurufnya(harus sama dangan sebelumnya): '))
enkripsi = open('d:\TeksSandi.txt', 'r')
sandi = enkripsi.read()
hasil = []
for huruf in sandi:
    kode = int(ord(huruf)) - geser
    hasil.append(chr(kode))
for kode in hasil:
    enkripsi = open('d:\TeksHasil.txt', 'a')
    enkripsi.write(kode)