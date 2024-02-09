#NAME:  Timofiy Kharchuk
#
#STUDENT NUMBER:  1008424
#
#ICS3U0 SECTION:  E
#
#OVERVIEW:  Converts inputted Fahrenheit temperature and outputs it in Celsius



# Gets input from user
fahrenheitTemperature = float(input("Enter temperature to be converted and press enter: "))

# Converts input to fahrenheit and rounds to 2 decimal places
celsiusTemperature = round((fahrenheitTemperature - 32) * 5/9, 2)

# Returns result
print(fahrenheitTemperature, "in celsius is:", celsiusTemperature)