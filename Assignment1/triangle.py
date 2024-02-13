#NAME:  Timofiy Kharchuk
#
#STUDENT NUMBER:  1008424
#
#ICS3U0 SECTION:  E
#
#OVERVIEW:  Prints a right triangle with the non-hypotenuse side lengths of the input

# Get desired side length from user
sideLength = int(input("Enter the side length and press enter: "))

# Adds some space between the prompt and the output
print("")

# Use 2 nested for loops in order to print the triangle
for i in range(sideLength):

    # Initializes the variable that will hold each row
    row = ""

    # Adds sideLength number of stars to the variable that holds the row value
    for j in range(i):
        row += " * "

    # Prints each row
    print(row)
