print "Enter five names, every name at own line: "
names = []
i = 1
j = 1

while i <= 5:
    names.append(raw_input())
    i += 1

print "The original list of names is:"
for name in names:
    print name,

print "\n"
print "The sorted list of names is:"
for name in sorted(names):
    print name,
