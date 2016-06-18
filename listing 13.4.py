def calculateTax(price, taxRate):
    total = price + (price * taxRate/100)
    return total

myPrice = float(raw_input("Enter a price: "))
myTax = float(raw_input("Enter a TAX: "))

totalPrice = calculateTax(myPrice, myTax)

print "price = ", myPrice, "Price with VAT = ", totalPrice
