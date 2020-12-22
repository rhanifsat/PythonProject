nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	     {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	     {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

def tabel(lst):
    i = 0
    print('=====================================')
    print('| NIM | NAMA        | N.MID | N.UAS |')
    print('-------------------------------------')
    i = 0
    while i < len(nilai):
        print('|', lst[i]['nim'], '|', lst[i]['nama'], ' ' * (10-len(lst[i]['nama'])), '| ', lst[i]['mid'], ' ' * (3-len(str(lst[i]['mid']))), '| ',  lst[i]['uas'], ' ' * (3-len(str(lst[i]['uas']))), '|')
        i += 1
    print('-------------------------------------')

tabel(nilai)