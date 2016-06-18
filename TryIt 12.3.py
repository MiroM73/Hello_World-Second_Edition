print "Enter five names, every name at own line: "
names = []
i = 1

while i <= 5:
    names.append(raw_input())
    i += 1

print "The third name you entered is:",names[2]
