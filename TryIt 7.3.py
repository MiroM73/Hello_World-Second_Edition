import sys

heslo = "miro"
heslou = raw_input('Zadaj heslo pre spustenie programu: ')
if heslo != heslou:
    sys.exit()

velkost_nadrze = float(raw_input('Zadajte velkost nadrze v litroch: '))
zostatok_paliva = float(raw_input('Zadajte zostatok paliva v percentach (polovica je 50, tristvrte je 75 atd.: '))
spotreba = float(raw_input('Zadajte spotrebu v litroch na 100 km: '))
vzdialenost_k_pumpe = float(raw_input('Zadajte vzdialenost k pumpe v km: '))

mame_paliva = velkost_nadrze * zostatok_paliva / 100
dojazd_paliva = 100 / spotreba * mame_paliva
dojazd_paliva_minus_5l = 100 / spotreba * (mame_paliva -5)
potrebujeme_paliva = vzdialenost_k_pumpe / 100 * spotreba

print "Velkost nadrze:",velkost_nadrze,"l"
print "Zostatok paliva:",zostatok_paliva,"%"
print "Spotreba litrov na 100 km:",spotreba
print "Vas dojazd je:",int(dojazd_paliva),"km"
print "Vas dojazd pri zachovani rezervy 5l:",int(dojazd_paliva_minus_5l),"km"
print "Najblizsia pumpa je vzdialena:",vzdialenost_k_pumpe,"km"

if dojazd_paliva_minus_5l < vzdialenost_k_pumpe:
    print "Natankujte hned, lebo k dalsej pumpe Vam nemusi vystacit palivo!"
else:
    print "Na dalsiu pumpu to zvladnete."
    
