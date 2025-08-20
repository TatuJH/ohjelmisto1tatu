#Tehtävä 3.1
paino = float(input("Kuinka pitkä kuha on senttimetreissä?"))
if paino < 37:
    print("Kuha on alimittainen "+str(37-paino)+" senttimetrillä. Laske se takaisin järveen.")
else:
    print("Hyvä saalis")

#Tehtävä 3.2
hytti = input("Mistä hyttiluokasta haluat tietoa? Valitse A, B, C tai LUX").lower()
if hytti == "a":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hytti == "b":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hytti == "c":
    print("C on ikkunaton hytti autokannen alapuolella.")
elif hytti == "lux":
    print("LUX on parvekkeellinen hytti yläkannella.")
else:
    print("Virheellinen hytti")

#Tehtävä 3.3
sukup = input("Mikä on biologinen sukupuolesi m/n?")
hemog = float(input("Entä hemoglobiiniarvosi g/l?"))
if sukup == "m":
    if hemog <= 195 and hemog >= 134:
        print("Hemoglobiiniarvosi on normaali")
    elif hemog > 195:
        print("Hemoglobiiniarvosi on korkea")
    elif hemog < 134:
        print("Hemoglobiiniarvosi on alhainen")
elif sukup == "n":
    if hemog <= 175 and hemog >= 117:
        print("Hemoglobiiniarvosi on normaali")
    elif hemog > 175:
        print("Hemoglobiiniarvosi on korkea")
    elif hemog < 117:
        print("Hemoglobiiniarvosi on alhainen")

#Tehtävä 3.4
vuosi = int(input("Mikä vuosi?"))
if vuosi % 100 == 0:
    if vuosi % 400 == 0:
        print("Vuosi on karkausvuosi")
elif vuosi % 4 == 0:
    print("Vuosi on karkausvuosi")
else:
    print("Vuosi ei ole karkausvuosi")

