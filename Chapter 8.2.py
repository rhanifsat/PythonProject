myString = "python adalah bahasa pemrograman yang menyenangkan"
print(myString)
hurufpenyusun = set(myString)
huruf = list(hurufpenyusun)
huruf.sort()
print("Huruf penyusunnya adalah", huruf)