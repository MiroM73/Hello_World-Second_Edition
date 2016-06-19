# my module contains the c_to_f() function
from my_module import *

celsius = float(raw_input("Enter a temperature in celsius: "))
fahrenheit = c_to_f(celsius)
print "That's ", fahrenheit, " degree Fahrenheit"

fahrenheit = float(raw_input("Enter a temperature in fahrenheit: "))
celsius = f_to_c(fahrenheit)
print "That's ", celsius, " degree Celsius"