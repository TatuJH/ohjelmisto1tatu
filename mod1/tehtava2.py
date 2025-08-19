import math

nimi = input("Mikä on nimesi?")
print("Hei, "+nimi)

sade = float(input("Mikä on ympyrän säde?"))
print("Ympyrän pinta-ala on ",math.pi*sade**2)

kanta = float(input("Mikä on suorakulmion kanta?"))
korkeus = float(input("Entä korkeus?"))
print("Suorakulmion piiri on ",kanta*2+korkeus*2," ja sen pinta ala on ",kanta*korkeus)

luvut = []
while len(luvut) < 3:
    luvut.append(int(input("Anna kokonaisluku")))
print("Lukujen summa on ",sum(luvut),", niiden keskiarvo on ",(sum(luvut)/3)," ja niiden tulo on ",)