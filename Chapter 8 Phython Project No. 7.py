buah = {
    'apel'  : 5000,
    'jeruk' : 8500,
    'mangga': 7800,
    'duku'  : 6500
}

def buahmahal(lst):
    lst1 = sorted(lst, key = lambda harga : harga[1])
    print('Buah termahal adalah', lst1[0])

buahmahal(buah)