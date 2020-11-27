bind    = int(input("Masukkan nilai Bahasa Indonesia (0-100): "))
ipa     = int(input("Masukkan nilai IPA              (0-100): "))
mat     = int(input("Masukkan nilai Matematika       (0-100): "))
status  = "Status Kelulusan:"
if (bind > 100) or (ipa > 100) or (mat > 100) or (bind < 0) or (ipa < 0) or (mat < 0):
    print("Maaf input ada yang tidak valid")
    print("Mohon coba kembali")
elif (bind < 60) or (ipa < 60) or (mat < 70):
    print(status, "TIDAK LULUS")
else:
    print(status, "LULUS")