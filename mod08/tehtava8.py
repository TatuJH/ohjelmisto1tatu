import mysql.connector
from geopy import distance

yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='tatu',
         password='Tietokannat1',
         autocommit=True
         )

#Tehtävä 8.1
def lentokentta(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident='{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print(tulos)
lentokentta(input("Anna lentokentän ICAO-koodi:"))

#Tehtävä 8.2
def lentokentat(maakoodi):
    sql = f"SELECT type, COUNT(*) AS 'Määrä' FROM airport WHERE iso_country='{maakoodi}' GROUP BY type"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print(tulos)
lentokentat(input("Anna maakoodi:"))

#Tehtävä 8.3
def etaisyys(maa1, maa2):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident='{maa1}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos1 = kursori.fetchall()
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident='{maa2}'"
    kursori.execute(sql)
    tulos2 = kursori.fetchall()
    print(distance.distance(tulos1, tulos2).km)
etaisyys(input("Anna 1. ICAO:"), input("Anna 2. ICAO:"))