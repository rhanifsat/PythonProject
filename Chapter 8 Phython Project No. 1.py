import time
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
    
lst = []
while True:
    try:
        bil = int(input("Masukkan bilangan bulat: "))
        lst.append(bil)
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
            lst.sort(reverse=True)
            time.sleep(2)
            print()
            print("Urutan semua bilangan dari yang terbesar adalah")
            time.sleep(2)
            print(lst)
            break
    except ValueError:
        print("Bukan bilangan bulat")
        timer()
        continue