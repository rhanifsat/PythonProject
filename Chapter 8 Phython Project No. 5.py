def kuadrat(bil):
    hsl = []
    i = 0
    for hasil in bil:
        hasil = bil[i] ** 2
        i += 1
        hsl.append(hasil)
    print("bil   =", lst)
    print("hasil =", hsl)

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
            kuadrat(lst)
            break
    except ValueError:
        print("Bukan bilangan bulat")
        timer()
        continue