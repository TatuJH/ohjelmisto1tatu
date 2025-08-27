import random
import math

#Tehtävä 6.1
def nopanheitto():
    return random.randint(1,6)
def noppa_main():
    luku = 0
    while luku != 6:
        luku = nopanheitto()
        print(luku)
noppa_main()

#Tehtävä 6.2
def nopanheitto2(tahkot):
    return random.randint(1,tahkot)
def noppa2_main():
    luku = 0
    tahkot = int(input("Monta tahkoa nopassa?"))
    while luku != tahkot:
        luku = nopanheitto2(tahkot)
        print(luku)
noppa2_main()

#Tehtävä 6.3
def muunnos(gallonat):
    return gallonat * 3785
def muunnos_main():
    gallonat = int(input("Monta gallonaa muunnetaan?"))
    while gallonat >= 0:
        print(muunnos(gallonat))
        gallonat = int(input("Monta gallonaa muunnetaan?"))
muunnos_main()

#Tehtävä 6.4
def luvut(lista):
    return sum(lista)
def luvut_main():
    lista = [1,2,3,4,5,6,7,8,9,10]
    print(luvut(lista))
luvut_main()

#Tehtävä 6.5
def luvut2(lista):
    uusilista = []
    for i in lista:
        if i % 2 == 0:
            uusilista.append(i)
    return uusilista
def luvut_main2():
    lista = [1,2,3,4,5,6,7,8,9,10]
    print(lista)
    print(luvut2(lista))
luvut_main2()

#Tehtävä 6.6
def pizza(d, hinta):
    return hinta/(math.pi*(d/2)**2)
def pizza_main():
    pizza1 = pizza(int(input("Anna ekan pizzan halkaisija")),int(input("Anna ekan pizzan hinta")))
    pizza2 = pizza(int(input("Anna tokan pizzan halkaisija")),int(input("Anna tokan pizzan hinta")))
    if pizza1 > pizza2:
        print("Toka pizza antaa paremman vastineen rahoillesi")
    else:
        print("Eka pizza antaa paremman vastineen rahoillesi")
pizza_main()