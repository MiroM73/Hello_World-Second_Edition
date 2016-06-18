dlzkam = float(raw_input("Zadaj dlzku miestnosti: "))
sirkam = float(raw_input("Zadaj_sirku mistnosti: "))
dlzkak = float(raw_input("Zadaj dlzku koberca: "))
sirkak = float(raw_input("Zadaj sirku koberca: "))
obsahm = dlzkam * sirkam
obsahk = dlzkak * sirkak

pocetk = obsahm / obsahk

print "Pri rozmeroch miestnosti",dlzkam,"x",sirkam,"a rozmeroch koberca",dlzkak,
print "x",sirkak,"budeme potrebovat",pocetk,"kobercov na pokrytie miestnosti."
