import sys
dictionary = {}
i = 1

while i == 1:
    addorlook = raw_input("Add or look up a word (a/l) or quit (q)? ")
    if addorlook == "a":
        word = raw_input("Type the word: ")
        definition = raw_input("Type the definition: ")
        dictionary[word] = definition
        print "Word added!"
    elif addorlook == "l":
        word = raw_input("Type the word: ")
        if word in dictionary:
            print dictionary[word]
        else:
            print "That word isn't in the dictionary yet."
    elif addorlook == "q":
        sys.exit()
