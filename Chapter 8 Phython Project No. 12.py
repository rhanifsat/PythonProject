buah = {
    'apel'  : 5000,
    'jeruk' : 8500,
    'mangga': 7800,
    'duku'  : 6500
}

for key, val in buah.items():
    print(key, ':', val, '/ kg')

while True:
    print()
    print('Menu:')
    print('A. Tambah data buah')
    print('B. Beli buah')
    print('C. Hapus data buah')
    print()
    pilih = input('Pilihan Anda: ')
    print()
    A = 'A'
    B = 'B'
    C = 'C'

    if (pilih == A):
        while True:
            tambahbuah = input('Masukkan nama buah        : ')
            if tambahbuah in buah:
                print('Buah', tambahbuah, 'sudah ada dalam daftar')
                print()
            else:
                tambahharga = int(input('Masukkan harga buah per Kg: '))
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
                        print(key, ':', val, '/ kg')
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
                print('Buah', nama, 'Tidak ada dalam daftar')
                print()
    elif (pilih == C):
        while True:
            hapusbuah = input('Masukkan nama buah: ')
            if hapusbuah in buah:
                while True:
                    print("Apakah anda yakin ingin menghapus", hapusbuah, "dari daftar?")
                    lanjut = input('(y/n)')
                    jadin = "n"
                    jadiy = "y"
                    if (lanjut == jadiy):
                        print()
                        del buah[hapusbuah]
                        for key, val in buah.items():
                            print(key, ':', val, '/ kg')
                        break
                    elif (lanjut == jadin):
                        break
                    else:
                        print("Input salah")
                if (lanjut == jadin):
                    break
                elif (lanjut == jadiy):
                    break
            else:
                print('Buah', hapusbuah, 'tidak ada dalam daftar')
    else:
        print('Tidak ada dalam menu')