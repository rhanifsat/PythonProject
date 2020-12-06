buah = {
    'apel'  : 5000,
    'jeruk' : 8500,
    'mangga': 7800,
    'duku'  : 6500
}

for key, val in buah.items():
    print(key, ':', val)

hargasementara = []
while True:
    print()
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