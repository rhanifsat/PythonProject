nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80}, 	      
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},       
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50}, 
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30}, 
	        {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]

def nilaitinggi(lst):
    i = 0
    lstakhir = []
    for nilai in lst:
        nilai = (round((lst[i]['mid'] + 2 * lst[i]['uas']) / 3,1), lst[i]['nim'], lst[i]['nama'])
        i += 1
        lstakhir.append(nilai)
    lstakhir.sort(reverse = True)
    print('Mahasiswa yang mendapatkan nilai tertinggi adalah', lstakhir[0][2], 'dengan nim', lstakhir[0][1], 'dengan perolehan nilai', lstakhir[0][0])

nilaitinggi(nilaiMhs)