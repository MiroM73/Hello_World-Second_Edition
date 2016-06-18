def calculateTax(price, taxRate):
    total = price + (price * taxRate/100)
    # because my_price variable is defined in this function later, nex line
    # of code will generate error, because the my_price variable is not defined yet
    # if my_price variable will not be defined or changed in function, this print
    # will be OK
    print "my price (inside the function) before the change= ", my_price
    my_price = 10000
    print "my price (inside the function) = ", my_price
    return total

my_price = float(raw_input("Enter a price: "))

totalPrice = calculateTax(my_price, 20)

print "price = ", my_price, "Price with VAT = ", totalPrice
print "my price (outside the function) = ", my_price
