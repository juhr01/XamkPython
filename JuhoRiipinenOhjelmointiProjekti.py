#Ohjelmointiprojekti - Juho Riipinen

#Tarkastetaan, onko käyttäjän syöte kokonaisluku
def kysyKokonaisluku(syote):
  while True:
    try:
      return int(input(syote))
    except ValueError:
      print("Anna vain kokonaislukuja!")
      print("")

#Tarkastetaan, onko käyttäjän syöte ollenkaan luku
def kysyLuku(syote):
  while True:
    try:
      return float(input(syote))
    except ValueError:
      print("Anna vain numeroita!")
      print("")  

#Osion 1 funktio
def Osio1():

  print("")
  print("Plus-laskin")
  
  luku1 = kysyKokonaisluku("Anna luku 1: ")
  luku2= kysyKokonaisluku("Anna luku 2: ")

  lukujenSumma = luku1 + luku2
  
  print("")
  print("Lukujen summa on: " + str(lukujenSumma))
  print("")

#Osion 2 funktio
def Osio2():
  
  def tuenLaskenta():
    tuki = kysyLuku("Anna tuen määrä: ")
    
    tukiVuodessa = kuukaudet * tuki
    
    print("Opintotukea vuodessa: " + str(tukiVuodessa))
  
  print("")
  print("Opintotukilaskuri")
  
  while True:
    kuukaudet = kysyKokonaisluku("Anna kokonaisten tukikuukausien määrä: ")
  
    if (kuukaudet < 1):
      print("Anna vähintään yksi kuukausi")
    elif (kuukaudet > 12):
      print("Anna korkeintaan 12 kuukautta")
    else:
      break
  
  tuenLaskenta()

#Osion 3 funktio
def Osio3():
  print("")
  print("Toiminnot:")
  print("1 - Plus-laskin")
  print("2 - Opintotukilaskuri")
  print("3 - Ohjeet")
  valinta = int(input("Valitse toiminto 1-3: "))
  print("")
  
  if (valinta == 1):
    Osio1()
  elif (valinta == 2):
    Osio2()
  elif (valinta == 3):
    Osio3()

#Osion 4 funktio
#def Osio4():
#  print("-- Osio 4 --")

#Osion 5 funktio
#def Osio5():
#  print("-- Osio 5 --")

#Ylle kirjoitettujen funktioiden kutsut ja kommentti siitä mitä opit kyseisessä osiossa:

#Epäselvyyksiä ei jäänyt tästä osiosta. Haasteita oli eniten syntaksien kanssa, sillä olen tottunut kirjoittamaan JavaScriptiä.
#Osio1()

#Osio ei ollut sinäänsä vaikea, mutta haasteita ilmeni toiminnoissa, jotka estävät ohjelman kaatumisen vääränlaisen käyttäjäsyötteen jälkeen.
#Eniten aikaa meni funktioiden luontiin, jotka tarkastavat, onko syöte kokonaisluku tai numero. Lisäksi haastavahkoa oli tarkastaa, oliko kuukaudet 1-12 ilman, että ohjelma pysähtyy tai toistaa itseään.
#Etsin tietoa ongelmien ratkaisuun mm. Stack Overflow -sivulta sekä Claudelta.
#Osio2()

#En juurikaan oppinut mitään uutta, kertasin vain koodin kirjoittamista/Pythonin syntaksia.
Osio3()

#Kommentoi osiossa käsiteltyjä asioita ja kerro mitä opit osiossa ja/tai mikä jäi epäselväksi.
#Osio4()

#Kommentoi osiossa käsiteltyjä asioita ja kerro mitä opit osiossa ja/tai mikä jäi epäselväksi.
#Osio5()