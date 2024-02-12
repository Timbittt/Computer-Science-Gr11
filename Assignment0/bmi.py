#NAME:  Timofiy Kharchuk
#
#STUDENT NUMBER:  1008424
#
#ICS3U0 SECTION:  E
#
#OVERVIEW:  Converts inputted height and weigh, converts to bmi and outputs the result

# get type of units from user
units = input("Enter type of units (M or Metric for Metric, I or Imperial for Imperial), and press enter:")

# prompt and get input based off of system, then calculate BMI
if units == "M" or units == "Metric":
    height = int(input("Enter your height in centimeters and press enter:"))
    weight = int(input("Enter your weight in kilograms and press enter:"))
    bmi = weight / (height/100)**2

elif units == "I" or units == "Imperial":
    height = int(input("Enter your height in inches and press enter:"))
    weight = int(input("Enter your weight in pounds and press enter:"))
    bmi = 703 * (weight / height**2)

else:
    print("ERROR: invalid input, restart program and enter a valid input")

# output rounded result
print("Based on the given measurements, your BMI is", round(bmi, 2))