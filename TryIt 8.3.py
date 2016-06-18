print "Which multiplication table would you like?"
multipl = int(raw_input())
print "How high do you want to go?"
high = int(raw_input())

print "Here is your table"
i = 1
while i <= high:
    print multipl, "x", i, "=", multipl * i
    i += 1
