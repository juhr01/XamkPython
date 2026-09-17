#Ohjelmointiprojekti - Juho Riipinen

#Osion 1 funktio
def Osio1():
  print("")
  print("Plus-laskin")
  
  print("Anna luku 1: ")
  input1 = int(input())
  
  print("Anna luku 2: ")
  input2= int(input())
  
  sumOfInputs = input1 + input2
  
  print("Lukujen summa on: " + str(sumOfInputs))
  print("")
  

#Osion 2 funktio
#def Osio2():
#  print("-- Osio 2 --")

#Osion 3 funktio
def Osio3():
  print("")
  print("Toiminnot:")
  print("1 - Ohjeet")
  print("2 - Plus-laskin")
  valinta = int(input("Valitse toiminto 1-2: "))
  print("")
  
  if (valinta == 1):
    Osio3()
  elif (valinta == 2):
    Osio1()

#Osion 4 funktio
#def Osio4():
#  print("-- Osio 4 --")

#Osion 5 funktio
#def Osio5():
#  print("-- Osio 5 --")

#Ylle kirjoitettujen funktioiden kutsut ja kommentti siitä mitä opit kyseisessä osiossa:

#Epäselvyyksiä ei jäänyt tästä osiosta. Haasteita oli eniten syntaksien kanssa, sillä olen tottunut kirjoittamaan JavaScriptiä.
#Osio1()

#Kommentoi osiossa käsiteltyjä asioita ja kerro mitä opit osiossa ja/tai mikä jäi epäselväksi.
#Osio2()

#En juurikaan oppinut mitään uutta, kertasin vain koodin kirjoittamista/Pythonin syntaksia.
Osio3()

#Kommentoi osiossa käsiteltyjä asioita ja kerro mitä opit osiossa ja/tai mikä jäi epäselväksi.
#Osio4()

#Kommentoi osiossa käsiteltyjä asioita ja kerro mitä opit osiossa ja/tai mikä jäi epäselväksi.
#Osio5()