dlzkam = float(raw_input("Zadaj dlzku miestnosti v metroch: "))
sirkam = float(raw_input("Zadaj_sirku mistnosti v metroch: "))
dlzkak = float(raw_input("Zadaj dlzku koberca v metroch: "))
sirkak = float(raw_input("Zadaj sirku koberca v metroch: "))
cena = float(raw_input("Zadaj cenu koberca za meter stvorcovy v €: "))
obsahm = dlzkam * sirkam
obsahk = dlzkak * sirkak

pocetk = obsahm / obsahk
cenak = obsahm * cena

print "Pri rozmeroch miestnosti",dlzkam,"x",sirkam,"co je",obsahm,"metrov stvorcovych",
print "a rozmeroch koberca",dlzkak,"x",sirkak,
print "budeme potrebovat",pocetk,"kobercov na pokrytie miestnosti."
print "Cena za koberce pri uvedenych rozmeroch bude",cenak,"€."
