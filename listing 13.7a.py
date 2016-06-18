def calculateTax(price, taxRate):
    global my_price
    total = price + (price * taxRate/100)
    print "my price (inside the function) before the change= ", my_price
    my_price = 10000
    print "my price (inside the function) = ", my_price
    return total

my_price = float(raw_input("Enter a price: "))

totalPrice = calculateTax(my_price, 20)

# vyriable my_price in print was changed in function calculateTax to value 10000
# but calculation of variable total was made before the change
print "price = ", my_price, "Price with VAT = ", totalPrice
print "my price (outside the function) = ", my_price
