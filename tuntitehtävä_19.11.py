#otetaan käyttöön arrow-kirjasto ajan käsittelyyn
import arrow

#määritetään nykyhetki muuttujaan
nykyhetki = arrow.now()

#tulostetaan tämänhetkinen vuosi
print("Nyt on vuosi " + str(nykyhetki.year))

#tulostetaan, mikä vuosi oli viisi vuotta sitten. kirjoitetut tulokset on käännetty suomeksi locale='fi' avulla.
print(str(nykyhetki.shift(years=-5).humanize(locale='fi')) + " oli vuosi " + str(nykyhetki.shift(years=-5).year))

#tulostetaan, mikä vuosi viime vuonna oli
print(str(nykyhetki.shift(years=-1).year) + " oli " + str(nykyhetki.shift(years=-1).humanize(locale='fi')))

#tulostetaan, mikä vuosi on ensi vuonna
print(str(nykyhetki.shift(years=1).humanize(locale='fi')) + " on vuosi " + str(nykyhetki.shift(years=1).year))

#ohjelma on joustava, sillä se tulostaa esimerkiksi vielä ensi vuonna oikeat tulokset




