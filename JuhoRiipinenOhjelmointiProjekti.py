#Ohjelmointiprojekti - Juho Riipinen

#Tarkastetaan, onko käyttäjän syöte kokonaisluku
def kysyKokonaisluku(syote):
  while True:
    try:
      #Jos syöte on kokonaisluku, palautetaan kokonaisluku
      return int(input(syote))
    #Jos syöte ei ole kokonaisluku, tulee ValueError ja tulostetaan viesti
    except ValueError:
      print("Anna vain kokonaislukuja!")
      print("")

#Tarkastetaan, onko käyttäjän syöte ollenkaan luku
def kysyLuku(syote):
  while True:
    try:
      #Jos syöte on integer- tai float-luku, palautetaan luku
      return float(input(syote))
    #Jos syöte ei ole luku, tulee ValueError ja tulostetaan viesti
    except ValueError:
      print("Anna vain numeroita!")
      print("")  

#Osion 1 funktio
def Osio1():

  print("")
  print("Plus-laskin")
  
  #Kysytään käyttäjältä luvut, ja tallennetaan ne muuttujiin "luku1" ja "luku2"
  luku1 = kysyKokonaisluku("Anna luku 1: ")
  luku2= kysyKokonaisluku("Anna luku 2: ")

  #Lasketaan syötettujen lukujen summa ja tallennetaan se muuttujaan lukujenSumma
  lukujenSumma = luku1 + luku2
  
  #Tulostetaan summa
  print("")
  print("Lukujen summa on: " + str(lukujenSumma))
  print("")

#Osion 2 funktio
def Osio2():

  print("")
  print("Opintotukilaskuri")
  
  #Kysytään käyttäjältä opintotuen määrä float-lukuna ja tallennetaan se muuttujaan "tuki"
  tuki = kysyLuku("Anna tuen määrä euroina: ")
  
  #Kysytään käyttäjältä loopissa tukikuukausien määrää niin pitkään, että ehdot täyttyvät
  while True:
    #Kysytään tukikuukausien määrä kokonaislukuna ja tallennetaan se muuttujaan "kuukaudet"
    kuukaudet = kysyKokonaisluku("Anna kokonaisten tukikuukausien määrä: ")
  
    #Jos syöte on alle 1, tulostetaan viesti ja aloitetaan loop alusta
    if (kuukaudet < 1):
      print("Anna vähintään yksi kuukausi")
      print("")
    #Jos syöte on yli 12, tulostetaan viesti ja aloitetaan loop alusta
    elif (kuukaudet > 12):
      print("Anna korkeintaan 12 kuukautta")
      print("")
    #Jos aiemmat ehdot eivät täyty, eli syöte on kokonaisluku väliltä 1-12, poistutaan while-loopista
    else:
      break
  
  #Kerrotaan opintotuen määrä tukikuukausilla ja tallennetaan tulo muuttujaan "tukiVuodessa"
  tukiVuodessa = kuukaudet * tuki   

  #Tulostetaan tulo
  print("Opintotukea vuodessa: " + str(tukiVuodessa) + " euroa")

#Osion 3 funktio
def Osio3():
  #Tulostetaan "käyttöliittymä"
  print("")
  print("Toiminnot:")
  print("1 - Plus-laskin")
  print("2 - Opintotukilaskuri")
  print("3 - Ohjeet")
  print("4 - Nelilaskin")
  print("5 - Alkuluvut")
  
  #Kysytään loputtomassa loopissa käyttältä ohjelman toimintoja
  #Jos valintaa vastaavaa funktiota ei ole, kysytään syötettä uudestaan
  while True:
    valinta = kysyKokonaisluku("Valitse toiminto 1-5: ")
    print("")
  
    #Kutsutaan syötettä vastaava funktio ja funktiokutsun jälkeen poistutaan loopista
    if (valinta == 1):
      Osio1()
      break
    elif (valinta == 2):
      Osio2()
      break
    elif (valinta == 3):
      Osio3()
      break
    elif (valinta == 4):
      Osio4()
      break
    elif (valinta == 5):
      Osio5()
      break

#Osion 4 funktio
def Osio4():
  print("Nelilaskin")
  #Kysytään käyttäjältä kaksi kokonaislukua ja tallennetaan ne muuttujiin
  luku1 = kysyKokonaisluku("Anna kokonaisluku 1: ")
  luku2 = kysyKokonaisluku("Anna kokonaisluku 2: ")
  
  #Tulostetaan lukujen summa, erotus, tulo, osamäärä ja jakojäännös
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
  #Kysytään käyttäjältä luku ja tallennetaa se muuttujaan
  luku = kysyKokonaisluku("Anna kokonaisluku tarkastaaksesi, onko se alkuluku: ")

  #Jos luku on alle 1 tai 1, se ei ole alkuluku
  if luku <= 1:
    print("Luku " + str(luku) + " ei ole alkuluku")
  #Jos luku on suurempi kuin 1, tehdään laskutoimitus tarkastamiseksi
  elif luku > 1:
    #Jaetaan annettu luku luvusta 2 eteenpäin itseensä asti
    #Jos jakojäännös on missä tahansa jakolaskussa 0, luku ei ole alkuluku, sillä alkuluku on ainoastaan jaollinen luvulla 1 ja itsellään
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