bind    = int(input("Masukan nilai Bahasa Indonesia (0-100): "))
ipa     = int(input("Masukan nilai IPA              (0-100): "))
mat     = int(input("Masukan nilai Matematika       (0-100): "))
status  = "Status Kelulusan:"
if (bind < 60) or (ipa < 60) or (mat < 70):
    print(status, "TIDAK LULUS")
else:
    print(status, "LULUS")