import math
AtoC = 795
jarakperltr = 12
totalkonsumsi = (AtoC/jarakperltr)
tankcpty = 50
timerefuel = (totalkonsumsi/tankcpty)

print("Kapasitas tangki   :",(tankcpty),"liter")
print("Total konsumsi     :",(totalkonsumsi),"liter")
print("Isi ulang sebanyak :",math.floor(timerefuel),"x")