def BMI(b, t):
    nilai = b / ((t / 100) * (t/ 100))
    print("BMI: ", nilai)
    if nilai < 18:
        print("KURUS")
    elif 18 <= nilai < 23:
        print("IDEAL")
    elif 23 <= nilai < 27:
        print("GEMUK")
    elif 27 <= nilai < 35:
        print("OBESITAS")
    elif nilai >= 35:
        print("OBESITAS MORBID")

berat  = int(input("Masukkan berat badan :     kg\b\b\b\b\b\b"))
tinggi = int(input("Masukkan tinggi badan:     cm\b\b\b\b\b\b"))
BMI(berat, tinggi)