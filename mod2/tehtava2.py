import math
import random

#Tehtävä 2.1
nimi = input("Mikä on nimesi?")
print("Hei, "+nimi)

#Tehtävä 2.2
sade = float(input("Mikä on ympyrän säde?"))
print("Ympyrän pinta-ala on ",math.pi*sade**2)

#Tehtävä 2.3
kanta = float(input("Mikä on suorakulmion kanta?"))
korkeus = float(input("Entä korkeus?"))
print("Suorakulmion piiri on ",kanta*2+korkeus*2," ja sen pinta ala on ",kanta*korkeus)

#Tehtävä 2.4
luvut = []
i = 1
while len(luvut) < 3:
    luvut.append(int(input("Anna kokonaisluku "+str(i))))
    i += 1
print("Lukujen summa on ",str(sum(luvut))+", niiden tulo on "+str(math.prod(luvut))+"ja niiden keskiarvo on "+str((sum(luvut)/3)))

#Tehtävä 2.5
massa = float(input("Monta leiviskää?"))*20*32*13.3
massa += float(input("Monta naulaa?"))*32*13.3
massa += float(input("Monta luotia?"))*13.3
print("Paino nykyaikana on "+str(int(massa/1000))+"kg "+str(round((massa)%1000,3))+"g")

#Tehtävä 2.6
print("Kolminumeroinen koodi on "+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)))
print("Nelinumeroinen koodi on "+str(random.randint(1,6))+str(random.randint(1,6))+str(random.randint(1,6))+str(random.randint(1,6)))


