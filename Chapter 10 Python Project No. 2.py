while True:
    myfile = open('d:\dataMhs.txt', 'a')
    nim =    input('Masukkan NIM       :')
    nama =   input('Masukkan Nama Mhs  :')
    alamat = input('Masukkan Alamat    :')
    frmt = '{}|{}|{}'.format(nim, nama, alamat)
    myfile.write(frmt + '\n')
    while True:
        lanjut = input("Input data lagi? (y/n) : ")
        jadin = "n"
        jadiy = "y"
        if (lanjut == jadin):
            myfile.close()
            break
        elif (lanjut == jadiy):
            myfile.close()
            break
        else :
            print("Input tidak tepat")
    if (lanjut == jadin):
        break