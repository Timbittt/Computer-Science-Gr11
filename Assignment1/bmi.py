#NAME:  Timofiy Kharchuk
#
#STUDENT NUMBER:  1008424
#
#ICS3U0 SECTION:  E
#
#OVERVIEW:  Converts inputted height and weigh, converts to bmi and outputs the result

# get type of units from user
units = input("Enter type of units (M or Metric for Metric, I or Imperial for Imperial), and press enter:")

# prompt and get input based off of system
if units == "M" or units == "Metric":
    height = input("Enter your height in centimeters and press enter:")
    weight = input("Enter your weight in kilograms and press enter:")

elif units == "I" or units == "Imperial":
    height = input("Enter your height in inches and press enter:")
    weight = input("Enter your weight in pounds and press enter:")

else:
    print("ERROR: invalid input, restart program and enter a valid input")

# calculate bmi
bmi = weight / height**2

# output result
print("Based on the given measurements, your BMI is", bmi)