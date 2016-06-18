print "Enter five names, every name at own line: "
names = []
i = 1
j = 1

while i <= 5:
    names.append(raw_input())
    i += 1

print "The names are",
for name in names:
    print name,
