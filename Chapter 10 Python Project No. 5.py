myfile = open('d:\databilangan.txt', 'r')
angka = myfile.readlines()
i = 0
while i < len(angka):
    split = angka[i].split('|')
    print(int(split[0]) + int(split[1]))
    i += 1