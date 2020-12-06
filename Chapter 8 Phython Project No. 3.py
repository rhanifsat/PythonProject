def timer():
    time.sleep(2)
    print("Coba lagi dalam")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)

import time
nama = []
while True:
    name = str(input("Masukkan nama mahasiswa: "))
    nama.append(name)
    while True:
        lanjut = input("Lagi (y/n)? : ")
        jadin = "n"
        jadiy = "y"
        if (lanjut == jadiy):
            break
        elif (lanjut == jadin):
            break
        else:
            print("Input salah")
            timer()
    if (lanjut == jadin):
        nama.sort()
        for nma in nama:
            print(nma, "({} karakter)".format(len(nma)))
        break