### TODO: Make code more readable and optimized

#NAME:  Timofiy Kharchuk
#
#STUDENT NUMBER:  1008424
#
#ICS3U0 SECTION:  E
#
#OVERVIEW:  Prints a multiplication table with side lengths of the input

sideLength = int(input("Enter the end of the multiplication table"))

for i in range(sideLength):
    row = ""
    
    for j in range(sideLength):
        #FIXME: Padding very buggy + code hard to read and inefficient
        value = str((i+1)*(j+1))
        padding = int((len(str((sideLength**2))) - len(value))/2)

        if len(value) % 2 == 1:
            value = " " * padding + value + " " * padding
        else:
            value = " " * (padding+1) + value + " " * padding
         
        row += value

    print(row)