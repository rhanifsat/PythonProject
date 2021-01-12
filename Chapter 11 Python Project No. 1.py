from datetime import *

def diffDate(x):
    skrg = datetime.today()
    tgl = datetime.strptime(x, '%Y-%m-%d')
    selisih = abs(skrg - tgl)
    return selisih.days

hari = diffDate('2021-09-28')
print(hari)