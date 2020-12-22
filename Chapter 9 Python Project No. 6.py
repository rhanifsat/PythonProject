nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	     {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	     {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

def tabel(lst):
    print('==============================================================')
    print('| NIM | NAMA        | N.MID | N.UAS | N.AKHIR |    STATUS    |')
    print('--------------------------------------------------------------')
    i = 0
    while i < len(nilai):
        nakhir = round((lst[i]['mid'] + 2 * lst[i]['uas']) / 3)
        status = 'LULUS' if nakhir >= 70 else 'TIDAK LULUS'
        spasinama =  ' ' * (10-len(lst[i]['nama']))
        spasimid = ' ' * (3-len(str(lst[i]['mid'])))
        spasiuas = ' ' * (3-len(str(lst[i]['uas'])))
        spasinakhir = ' ' * (4-len(str(nakhir)))
        spasistatus = ' ' * (11-len(status))
        print('|', lst[i]['nim'], '|', lst[i]['nama'], spasinama, '| ', lst[i]['mid'], spasimid, '| ',  lst[i]['uas'], spasiuas, '|  ', nakhir, spasinakhir, '|', status, spasistatus, '|'
        )
        i += 1
    print('--------------------------------------------------------------')

tabel(nilai)