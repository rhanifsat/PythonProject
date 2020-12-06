import time
def timer():
    time.sleep(2)
    print("Coba lagi dalam")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)

sayur = ['bayam', 'kangkung', 'wortel', 'selada']

while True:
    print()
    print('Menu:')
    print('A. Tambah data sayur')
    print('B. Hapus data sayur')
    print('C. Tampilkan data sayur')
    print()
    pilih = input('Pilihan Anda: ')
    A = 'A'
    B = 'B'
    C = 'C'

    if (pilih == A):
        while True:
            tambahsayur = input('Masukkan nama sayur: ')
            sayur.append(tambahsayur)
            lanjut = input('Lanjut (y/n): ')
            lanjutn = 'n'
            lanjuty = 'y'
            if (lanjut == lanjuty):
                continue
            elif (lanjut == lanjutn):
                break
    elif (pilih == B):
        try:
            while True:
                hapussayur = input('Masukkan nama sayur: ')
                sayur.remove(hapussayur)
                lanjut = input('Lanjut (y/n): ')
                lanjutn = 'n'
                lanjuty = 'y'
                if (lanjut == lanjuty):
                    continue
                elif (lanjut == lanjutn):
                    break
        except ValueError:
            print()
            print('!!!DATA TIDAK DITEMUKAN!!!')
            timer()
    elif (pilih == C):
        print(sayur)
        lanjut = input('Kembali ke menu (y/n): ')
        lanjutn = 'n'
        lanjuty = 'y'
        if (lanjut == lanjuty):
            continue
        elif (lanjut == lanjutn):
            break
    else:
        print('Tidak ada dalam menu')
        timer()