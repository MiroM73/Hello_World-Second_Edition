pohlavie = raw_input("Vase pohlavie M (Muz) alebo Z (Zena): ")
if pohlavie != "Z":
    print "Dakujeme za Vas zaujem, hladame vsak dievcata."
    exit
elif pohlavie == "Z":
    vek = raw_input("Zadajte Vas vek: ")
    if 10 <= vek <= 12:
        print "Super, poslite nam prihlasku."
    else:
        print "Je nam luto, ale Vas vek",vek,"rokov nie je v pozadovanom rozpati 10 az 12 rokov."
        
