# my module contains the c_to_f() function
import my_module

celsius = float(raw_input("Enter a temperature in celsius: "))
fahrenheit = my_module.c_to_f(celsius)
print "That's ", fahrenheit, " degree Fahrenheit"