from datetime import *

def addDataPnjm(kode, nama, judul, tglpnjm, tglkmbl):
    frmt = '{}|{}|{}|{}|{}'.format(kode, nama, judul, tglpnjm, tglkmbl)
    dftr.write(frmt)
    dftr.write('\n')

while True:
    dftr  = open('d:\DataPinjamanPerpus.dat', 'a')
    kode  = input('Masukkan Kode Member  : ')
    nama  = input('Masukkan Nama Member  : ')
    judul = input('Masukkan Judul Buku   : ')
    tglpnjm = date.today()
    tglkmbl = tglpnjm + timedelta(days=7)
    addDataPnjm(kode, nama, judul, tglpnjm, tglkmbl)
    while True:
        lanjut = input("Input data lagi? (y/n) : ")
        jadin = "n"
        jadiy = "y"
        if (lanjut == jadin):
            dftr.close()
            break
        elif (lanjut == jadiy):
            dftr.close()
            break
        else :
            print("Input tidak tepat")
    if (lanjut == jadin):
        break