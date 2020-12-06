buah = {
    'apel'  : 5000,
    'jeruk' : 8500,
    'mangga': 7800,
    'duku'  : 6500
}

for key, val in buah.items():
    print(key, ':', val)
print()

while True:
    nama = input('Nama buah yang dibeli : ')
    if nama in buah:
        nama = buah[nama]
        berat = float(input('Berapa Kg             : '))
        harga = nama *  berat
        print('--------------------------------')
        print('Total harga           :', harga)
        break
    else:
        print('Tidak ada dalam daftar')
        print()