print "Which multiplication table would you like?"
multipl = int(raw_input())
print "Here is your table"
i = 1
while i <= 10:
    print multipl, "x", i, "=", multipl * i
    i += 1
