cena_tovaru = float(raw_input('Zadajte cenu tovaru v eurach: '))

if cena_tovaru <= 10:
    cena_po_zlave = cena_tovaru * 0.9
    zlava = 10
elif cena_tovaru > 10:
    cena_po_zlave = cena_tovaru * 0.8
    zlava = 20

print "Zlava je",zlava,"%."
print "Vasa cena po zlave je:",cena_po_zlave,"€."
