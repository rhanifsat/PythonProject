buah = {
    'apel'  : 5000,
    'jeruk' : 8500,
    'mangga': 7800,
    'duku'  : 6500
}

for key, val in buah.items():
    print(key, ':', val)

while True:
    print()
    print('Menu:')
    print('A. Tambah data buah')
    print('B. Beli buah')
    print()
    pilih = input('Pilihan Anda: ')
    print()
    A = 'A'
    B = 'B'

    if (pilih == A):
        while True:
            tambahbuah = input('Masukkan nama buah: ')
            if tambahbuah in buah:
                print('Buah', tambahbuah, 'sudah ada dalam daftar')
                print()
            else:
                tambahharga = int(input('Masukkan harga buah: '))
                buah[tambahbuah] = tambahharga
                while True:
                    lanjut = input('Tambah lagi (y/n)?: ')
                    lanjutn = 'n'
                    lanjuty = 'y'
                    if (lanjut == lanjuty):
                        break
                    elif (lanjut == lanjutn):
                        break
                    else:
                        print('input salah')
                if (lanjut == lanjutn):
                    print()
                    for key, val in buah.items():
                        print(key, ':', val)
                    break
    elif (pilih == B):
        hargasementara = []
        while True:
            nama = input('Nama buah yang dibeli : ')
            if nama in buah:
                nama = buah[nama]
                berat = float(input('Berapa Kg             : '))
                harga = nama *  berat
                hargasementara.append(harga)
                while True:
                    lanjut = input("Beli buah lagi (y/n)? : ")
                    jadin = "n"
                    jadiy = "y"
                    if (lanjut == jadiy):
                        break
                    elif (lanjut == jadin):
                        break
                    else:
                        print("Input salah")
                if (lanjut == jadin):
                    final = sum(hargasementara)
                    print('--------------------------------')
                    print('Total harga           :', final)
                    break
            else:
                print('Tidak ada dalam daftar')
                print()
    else:
        print('Tidak ada dalam menu')