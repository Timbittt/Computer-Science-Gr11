#NAME:  Timofiy Kharchuk
#
#STUDENT NUMBER:  1008424
#
#ICS3U0 SECTION:  E
#
#OVERVIEW:  Prints a square of stars with side lengths of the input

# Get desired side length from user
sideLength = int(input("Enter the side length and press enter: "))

# Adds some space between the prompt and the output
print("")

# Use 2 nested for loops in order to print a square with sideLength width and height
for i in range(sideLength):
    # Prints each row with sideLength
    print(" * " * sideLength)
