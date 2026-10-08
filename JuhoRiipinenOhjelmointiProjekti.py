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

  print("")
  print("Opintotukilaskuri")
  
  tuki = kysyLuku("Anna tuen määrä euroina: ")
  
  while True:
    kuukaudet = kysyKokonaisluku("Anna kokonaisten tukikuukausien määrä: ")
  
    if (kuukaudet < 1):
      print("Anna vähintään yksi kuukausi")
      print("")
    elif (kuukaudet > 12):
      print("Anna korkeintaan 12 kuukautta")
      print("")
    else:
      break
  
  tukiVuodessa = kuukaudet * tuki   
  print("Opintotukea vuodessa: " + str(tukiVuodessa) + " euroa")

#Osion 3 funktio
def Osio3():
  print("")
  print("Toiminnot:")
  print("1 - Plus-laskin")
  print("2 - Opintotukilaskuri")
  print("3 - Ohjeet")
  print("4 - Nelilaskin")
  print("5 - Alkuluvut")
  valinta = int(input("Valitse toiminto 1-5: "))
  print("")
  
  if (valinta == 1):
    Osio1()
  elif (valinta == 2):
    Osio2()
  elif (valinta == 3):
    Osio3()
  elif (valinta == 4):
    Osio4()
  elif (valinta == 5):
    Osio5()

#Osion 4 funktio
def Osio4():
  luku1 = kysyKokonaisluku("Anna kokonaisluku 1: ")
  luku2 = kysyKokonaisluku("Anna kokonaisluku 2: ")
  
  print("")
  print(str(luku1) + " + " + str(luku2) + " = " + str(luku1 + luku2))
  print(str(luku1) + " - " + str(luku2) + " = " + str(luku1 - luku2))
  print(str(luku2) + " - " + str(luku1) + " = " + str(luku2 - luku1))
  print(str(luku1) + " * " + str(luku2) + " = " + str(luku1 * luku2))
  print(str(luku1) + " / " + str(luku2) + " = " + str(luku1 / luku2))
  print(str(luku2) + " / " + str(luku1) + " = " + str(luku2 / luku1))
  print(str(luku1) + " % " + str(luku2) + " = " + str(luku1 % luku2))
  print(str(luku2) + " % " + str(luku1) + " = " + str(luku2 % luku1))
  

#Osion 5 funktio
def Osio5():
  print("Alkuluvut")
  luku = kysyKokonaisluku("Anna kokonaisluku tarkastaaksesi, onko se alkuluku: ")

  if luku <= 1:
    print("Luku " + str(luku) + " ei ole alkuluku")
  elif luku > 1:
    for i in range(2, luku):
      if (luku % i) == 0:
        print("Luku " + str(luku) + " ei ole alkuluku")
        break
    else:
      print("Luku " + str(luku) + " on alkuluku")
  else:
    print("Luku " + str(luku) + " ei ole alkuluku")
    
#Ylle kirjoitettujen funktioiden kutsut ja kommentti siitä mitä opit kyseisessä osiossa:

#Epäselvyyksiä ei jäänyt tästä osiosta. Haasteita oli eniten syntaksien kanssa, sillä olen tottunut kirjoittamaan JavaScriptiä.
#Osio1()

#Osio ei ollut sinäänsä vaikea, mutta haasteita ilmeni toiminnoissa, jotka estävät ohjelman kaatumisen vääränlaisen käyttäjäsyötteen jälkeen.
#Eniten aikaa meni funktioiden luontiin, jotka tarkastavat, onko syöte kokonaisluku tai numero. Päädyin tekemään funktiot, koska lukuja tullaan kysymään lähes kaikissa ohjelman osissa. Lisäksi haastavahkoa oli tarkastaa, oliko kuukaudet 1-12 ilman, että ohjelma pysähtyy tai toistaa itseään.
#Etsin tietoa ongelmien ratkaisuun Pythonin dokumentaatiosta (https://docs.python.org/3/tutorial/errors.html#handling-exceptions).
#Osio2()

#En juurikaan oppinut mitään uutta, kertasin vain koodin kirjoittamista/Pythonin syntaksia.
Osio3()

#En oppinut tässäkään osiossa uusia asioita, kertasin vain operaattoreiden käyttöä.
#Osio4()

#Osio ei ollut vaikea, mutta laskin alkulukuja ohjelmalla ensimmäistä kertaa. Tietoa etsin Programiz-sivulta (https://www.programiz.com/python-programming/examples/prime-number).
#Osio5()