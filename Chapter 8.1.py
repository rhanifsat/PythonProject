import time
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
print("a =", a)
print("b =", b)
time.sleep(2)

print("Sisipkan nilai 10 ke dalam indeks ke-3 dari a, dan 15 ke dalam indeks ke-2 dari b")
print()
time.sleep(3)
a.insert(3, 10)
b.insert(2, 15)
print("a =", a)
print("b =", b)
time.sleep(2)

print("Sisipkan nilai 4 ke indeks terakhir dari a, dan 8 ke indeks terakhir dari b")
print()
time.sleep(3)
a.append(4)
b.append(8)
print("a =", a)
print("b =", b)
time.sleep(2)

print("Kemudian lakukan sorting secara ascending pada list a dan b")
print()
time.sleep(3)
a.sort()
b.sort()
print("a =", a)
print("b =", b)
time.sleep(2)

print("Buatlah list c yang elemennya merupakan sublist dari a (mulai dari indeks ke 0 s/d 7), dan") 
print("list d yang elemennya merupakan sublist dari b (mulai indeks ke 2 s/d 9)")
print()
time.sleep(3)
c = a[0:8]
d = b[2:10]
print("c =", c)
print("d =", d)
time.sleep(2)

print("Buatlah serangkaian langkah untuk mendapatkan list e yang elemennya merupakan hasil")
print("penjumlahan dari setiap elemen c dan d yang bersesuaian indeksnya.")
print()
time.sleep(3)
i = 0
e = []
for lst in c:
    lst = c[i] + d[i]
    i += 1
    e.append(lst)
print("e =", e)
time.sleep(2)

print("Ubahlah list e ke dalam tuple")
print()
time.sleep(3)
etupel = tuple(e)
print("e =", etupel)
time.sleep(2)

print("Carilah nilai min, maks, dan jumlah seluruh elemen dari e")
print()
time.sleep(3)
print("Nilai minimum =", min(e))
print("Nilai maksimum =", max(e))
print("Jumlah nilai seluruhnya =", sum(e))