#Tehtävä 7.1
kuukaudet = ("talvi","talvi","kevät","kevät","kevät","kesä","kesä","kesä","syksy","syksy","syksy","talvi")
print(kuukaudet[int(input("Anna kuukauden numero"))-1])

#Tehtävä 7.2
nimet = set()
nimi = input("Anna nimi tai paina enteriä lopettaaksesi")
while nimi != "":
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)
    nimi = input("Anna nimi tai paina enteriä lopettaaksesi")
for i in nimet:
    print(i)

#Tehtävä 7.3
lentoasema = {}
paatos = input("Haluatko lisätä (a), hakea (s) vai lopettaa (q)?")
while paatos != "q":
    if paatos== "a":
        lentoasema[input("Anna lentoaseman ICAO-koodi")] = input("Anna lentoaseman nimi")
    if paatos == "s":
        print(lentoasema[input("Anna lentoaseman ICAO-koodi")])
    paatos = input("Haluatko lisätä (a), hakea (s) vai lopettaa (q)?")

