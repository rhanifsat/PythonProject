from datetime import *

def diffDate(x):
    frmt = '%Y-%m-%d'
    skrg = datetime.today()
    tgl = datetime.strptime(x, frmt)
    selisih = skrg - tgl
    return selisih.days

def denda(x):
    if x >= 0:
        denda = x * 2000
    elif x <= 0:
        denda = x * 0
    return denda

member = {}
dftr = open('d:\DataPinjamanPerpus.dat', 'r')
data = dftr.readlines()
i = 0
lst = []
while i < len(data):
    split = data[i].split('|')
    value = (split[1], split[2], split[3], split[4])
    lst = list(value)
    member.update({split[0] : lst})
    i += 1

kode = input('Masukkan Kode Member: ')
if kode in member:
    kmbl   = date.today()
    trlmbt = diffDate(member[kode][3].strip())
    print('Data Pinjaman Buku')
    print('Kode Member              :', kode)
    print('Nama Member              :', member[kode][0])
    print('Judul Buku               :', member[kode][1])
    print('Tanggal Mulai Peminjaman :', member[kode][2])
    print('Tanggal Maks Peminjaman  :', member[kode][3])
    print('Tanggal Pengembalian     :', kmbl)
    print('Terlambat                :', trlmbt)
    print('Denda                    : Rp', denda(trlmbt))
else:
    print('Data Tidak Ditemukan')