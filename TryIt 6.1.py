import easygui

#easygui.msgbox ("This program converts Fahrenheit to Celsius.")
fahrenheit = float(easygui.enterbox(msg="Type in a temperature in Fahrenheit: ",title="This program converts Fahrenheit to Celsius."))
celsius = float(5)/9 * (fahrenheit - 32)
easygui.msgbox ("That is " + str(celsius) + " degrees Celsius.")

