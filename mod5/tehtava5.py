import random

#Tehtävä 5.1
nopat = int(input("Monta arpakuutiota heitetään?"))
summa = 0
for i in range(0,nopat):
    summa += random.randint(1,6)
print(f"Arpakuutioiden summa on {summa}.")

#Tehtävä 5.2
luvut = []
luku = input("Anna jokin luku")
while luku != "":
    luku = int(luku)
    luvut.append(luku)
    luku = input("Anna jokin luku tai lopeta enterillä")
luvut.sort(reverse=True)
for i in range(0,5):
    print(luvut[i])

#Tehtävä 5.3
luku = int(input("Anna jokin kokonaisluku"))
alkuluku = True
if luku >= 2:
    for i in range(2,luku):
        if luku % i == 0:
            alkuluku = False
    if alkuluku:
        print("Lukusi on alkuluku")
    else:
        print("Lukusi ei ole alkuluku")
else:
    print("Lukusi ei ole alkuluku")

#Tehtävä 5.4
kaupungit = []
for i in range(0,5):
    kaupungit.append(input("Anna jokin kaupunki"))
for i in range(0,len(kaupungit)):
    print(kaupungit[i])