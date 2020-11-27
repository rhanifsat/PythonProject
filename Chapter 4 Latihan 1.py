tarifpertama = 200000
tarifberikutnya = 10000
jammulai = 6
jamselesai = 23
menitmulai = 00
menitselesai = 50

durasisewa = ((jamselesai-jammulai)+(menitselesai-menitmulai)/60)
durasisewafinal = (int(durasisewa))
tambahanjam = (durasisewafinal-12)
biayatambahan = (tambahanjam*tarifberikutnya)
totalbiaya = (tarifpertama+biayatambahan)

print("           Tarif Sewa            ")
print("=================================")
print("| 12 Jam Pertama    : Rp",(tarifpertama),"|")
print("| Perjam berikutnya : Rp ",(tarifberikutnya),"|")
print("=================================")
print("Pukul Ambil   :",(jammulai),":",(menitmulai))
print("Pukul Kembali :",(jamselesai),":",(menitselesai))

print("Tambahan Jam :",(tambahanjam))
print("Total durasi :",(durasisewafinal))

print("Biaya Pertama  : Rp",(tarifpertama))
print("Biaya Tambahan : Rp ",(biayatambahan))
print("==========================(+)")
print("Total Biaya    : Rp",(totalbiaya))