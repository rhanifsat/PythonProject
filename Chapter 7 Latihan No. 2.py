try:
    direktori = input("masukkan direktori file: ")
    file = open(direktori, "r")
    while True:
        file = open(direktori, "a")
        tambah = input("Data yang mau ditambahkan: ")
        file.write(tambah)
        while True:
            lanjut = input("Mau lagi (y/n) : ")
            jadin = "n"
            jadiy = "y"
            if (lanjut == jadin):
                file.close()
                break
            elif (lanjut == jadiy):
                file.close()
                break
            else :
                print("Input tidak tepat")
        if (lanjut == jadin):
            break
except FileNotFoundError:
    print("File tidak ditemukan")
    print("Mohon coba kembali")