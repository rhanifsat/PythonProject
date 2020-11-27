import math
jamstart = 6
mntstart = 0
dtkstart = 0
AtoB = 125
BtoC = 256
speedAtoB = 62
speedBtoC = 70

jamBrest = 0
mntBrest = 45
dtkBrest = 0

jamAtoB = (math.floor(AtoB/speedAtoB))
mntAtoB = (math.floor(((AtoB/speedAtoB)-(math.floor(AtoB/speedAtoB)))*60))
dtkAtoB = (math.floor(((((AtoB/speedAtoB)-(math.floor(AtoB/speedAtoB)))*60)-(math.floor(((AtoB/speedAtoB)-(math.floor(AtoB/speedAtoB)))*60)))*60))

jamBtoC = (math.floor(BtoC/speedBtoC))
mntBtoC = (math.floor(((BtoC/speedBtoC)-(math.floor(BtoC/speedBtoC)))*60))
dtkBtoC = (math.floor(((((BtoC/speedBtoC)-(math.floor(BtoC/speedBtoC)))*60)-(math.floor(((BtoC/speedBtoC)-(math.floor(BtoC/speedBtoC)))*60)))*60))

durasijam = (jamAtoB+jamBrest+jamBtoC)
durasimnt = (mntAtoB+mntBrest+mntBtoC)
durasidtk = (dtkAtoB+dtkBrest+dtkBtoC)

mnttojam = (math.floor(durasimnt/60))
dtktomnt = (math.floor(durasidtk/60))
sisamnt = (math.floor(((durasimnt/60)-(mnttojam))*60))
sisadtk = (math.floor(((durasidtk/60)-(dtktomnt))*60))

finaljam = (durasijam+mnttojam)
finalmnt = (sisamnt+dtktomnt)
finaldtk = (sisadtk)


print("Berangkat Pukul   =",(jamstart),":",(mntstart),":",(dtkstart))
print("Lama perjalanan   =",(durasijam),"jam",(durasimnt),"menit",(durasidtk),"detik")
print("Durasi Final      =",(finaljam),":",(finalmnt),":",(finaldtk))
print("Tiba Pukul        =",(jamstart+finaljam),":",(mntstart+finalmnt),":",(dtkstart+finaldtk))