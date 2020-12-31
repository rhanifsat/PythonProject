dataMhs = []
myfile = open('d:\dataMhs.txt', 'r')
data = myfile.readlines()
i = 0
while i < len(data):
    split = data[i].split('|')
    a = dict(nim = split[0], nama = split[1], alamat = split[2].strip())
    dataMhs.append(a)
    i += 1
print(dataMhs)