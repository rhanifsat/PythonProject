mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

i = 0
print('============================================================')
print('| NIM  |    NAMA MAHASISWA     | TGL LAHIR  | TEMPAT LAHIR |')
print('------------------------------------------------------------')
while i < len(mhs):
    split = mhs[i].split(':')
    splittgl = split[2].split('-')
    spasinama = ' ' * (20 - len(split[1]))
    spasitmpt = ' ' * (11 - len(split[3]))
    print('|', split[0], '|', split[1], spasinama, '|', splittgl[2]+'/'+splittgl[1]+'/'+splittgl[0], '|', split[3], spasitmpt, '|')
    i += 1
print('------------------------------------------------------------')