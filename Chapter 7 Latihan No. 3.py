print("------------------------------")
print("   PROGRAM HITUNG RATA-RATA   ")
print("------------------------------")
sum = 0
banyak = 0
while True:
    try:
        bil = int(input("Masukkan bilangan bulat: "))
        sum = sum + bil
        lanjut = input("Lagi (y/n)? : ")
        jadin = "n"
        banyak = banyak + 1
        if (lanjut == jadin):
            rata2 = sum / banyak
            print("Rata-rataya adalah: ", rata2)
            break
    except ValueError:
        print("Bukan bilangan bulat")
        continue