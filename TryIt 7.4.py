import sys

heslo = "mirom"
heslou = raw_input("Zadaj heslo: ")
if heslo != heslou:
    print("Nespravne heslo!")
    sys.exit()
else:
    print("Spravne heslo!")
