import easygui
meno = easygui.enterbox ("Zadaj svoje meno")
adresa = easygui.enterbox ("Zadaj ulicu")
mesto = easygui.enterbox ("Zadaj mesto")
stat = easygui.enterbox("Zadaj stat")
psc = easygui.enterbox ("Zadaj PSC")
cela_adresa = meno + '\n' + adresa + '\n' + mesto + ", " + stat + '\n' + psc
easygui.msgbox (cela_adresa,"Tvoja cela adresa:")
