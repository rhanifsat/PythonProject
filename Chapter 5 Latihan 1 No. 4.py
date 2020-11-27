# Gol   Gaji Pokok  Potongan
# A     10.000.000  2.5%
# B      8.500.000  2.0%
# C      7.000.000  1.5%
# D      5.500.000  1.0%

kode = input("Masukkan Kode Karyawan: ")
nama = input("Masukkan Nama Karyawan: ")
gol  = str(input("masukkan Golongan     : "))
golA = "A"
golB = "B"
golC = "C"
golD = "D"
A = 10000000
B =  8500000
C =  7000000
D =  5500000
potA = A * 2.5 / 100
potB = B * 2.0 / 100
potC = C * 1.5 / 100
potD = D * 1.0 / 100

print("=========================================")
print("       STRUK RINCIAN GAJI KARYAWAN       ")
print("-----------------------------------------")
print("Nama Karyawan:", nama, "( Kode:", kode, ")")
print("Golongan     :", gol)
print("-----------------------------------------")

if (gol == golA):
    print("Gaji Pokok   : Rp", A)
    print("Potongan 2.5%: Rp  ", potA)
    print("_________________________________________(-)")
    print("Gaji Bersih  : Rp ", A - potA)
elif (gol == golB):
    print("Gaji Pokok   : Rp", B)
    print("Potongan 2.0%: Rp ", potB)
    print("_________________________________________(-)")
    print("Gaji Bersih  : Rp", B - potB)
elif (gol == golC):
    print("Gaji Pokok   : Rp", C)
    print("Potongan 1.5%: Rp ", potC)
    print("_________________________________________(-)")
    print("Gaji Bersih  : Rp ", C - potC)
elif (gol == golD):
    print("Gaji Pokok   : Rp", D)
    print("Potongan 1.0%: Rp ", potD)
    print("_________________________________________(-)")
    print("Gaji Bersih  : Rp", D - potD)