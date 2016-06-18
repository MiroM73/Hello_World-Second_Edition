print "Enter five names, every name at own line: "
names = []
i = 1

while i <= 5:
    names.append(raw_input())
    i += 1

print "The names are",
for name in names:
    print name,

print

replace = int(raw_input("Replace one name. Which one? (1-5): ")) - 1
newname = raw_input("New name: ")

names[replace] = newname

print "The names are",
for name in names:
    print name,
