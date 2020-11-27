def jarak(v0, t, a):
    st = v0 * t + 1/2 * a * (t ** 2)
    print('t=', t, ', S(t)=', st,)

v0 = int(input("Masukkan ketepatan awal: "))
a  = int(input("Masukkan perceratan: "))
t  = 0
while True:
    t += 1
    if (t > 10):
        break
    jarak(v0, t, a)