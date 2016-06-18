numBlocks = int(raw_input("How many blocks of stars do you want? "))
numLines = int(raw_input("How many lines of stars do you want? "))
numStars = int(raw_input("How many stars do you want? "))
for blocks in range (0, numBlocks):
    for lines in range (0, numLines):
        for stars in range (0, numStars):
            print "*",
        print
    print
