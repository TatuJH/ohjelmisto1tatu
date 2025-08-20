import random

#Tehtävä 4.1
luvut = []
i = 1
while i < 1000:
    if i % 3 == 0:
        luvut.append(i)
    i += 1
print(luvut)

#Tehtävä 4.2
tuumat = 0.0
while tuumat >= 0:
    tuumat = float(input("Anna positiivinen tuumamäärä tai negatiivinen lopettaaksesi"))
    if tuumat >= 0:
        print(str(tuumat)+" tuumaa on "+str(tuumat*2.54)+" senttimetriä")

#Tehtävä 4.3
luvut = []
luku = 0
while luku != "":
    luku = input("Anna luku tai paina enteriä lopettaaksesi")
    if luku != "":
        luvut.append(int(luku))
print("Pienin syöttämäsi luku oli "+str(min(luvut))+" ja suurin syöttämäsi luku oli "+str(max(luvut)))

#Tehtävä 4.4
luku = random.randint(1,10)
arvaus = 0
while arvaus != luku:
    arvaus = int(input("Arvaa numero 1-10"))
    if luku - arvaus < 0:
        print("Liian suuri arvaus")
    elif arvaus - luku < 0:
        print("Liian pieni arvaus")
    else:
        print("Oikein")

#Tehtävä 4.5
tunnus = "python"
salis = "rules"
tunnusarvaus = ""
salisarvaus = ""
arvaukset = 0
while arvaukset < 5 and (tunnusarvaus != tunnus or salisarvaus != salis):
    tunnusarvaus = input("Syötä käyttäjätunnus")
    salisarvaus = input("Syötä salasana")
    arvaukset += 1
    if tunnusarvaus == tunnus and salisarvaus == salis:
        print("Tervetuloa")
if arvaukset == 5:
    print("Pääsy evätty")

#Tehtävä 4.6
pistex = 0
pistey = 0
monta = int(input("Monta pistettä arvotaan?"))
pisteita = 0
i = 0
while i < monta:
    pistex=random.random()
    pistey=random.random()
    if pistex**2+pistey**2 < 1:
        pisteita += 1
    i += 1
print(4*pisteita/monta)

