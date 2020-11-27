direktori = input("masukkan direktori file: ")

file = open(direktori, "r")
print("Isi file", direktori, "adalah:")
print(file.read())