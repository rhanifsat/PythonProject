buah = {
    'apel'  : 5000,
    'jeruk' : 8500,
    'mangga': 7800,
    'duku'  : 6500
}
def rata2(lst):
    jumlah = []
    i = 0
    for harga in lst:
        harga = (lst[harga])
        jumlah.append(harga)
        i += 1
    print('Rata-rata harga buah adalah', (sum(jumlah) / i))

rata2(buah)