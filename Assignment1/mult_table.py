#NAME:  Timofiy Kharchuk
#
#STUDENT NUMBER:  1008424
#
#ICS3U0 SECTION:  E
#
#OVERVIEW:  Prints a multiplication table with side lengths of the input

                                                                        
sideLength = int(
    input("Enter the end of the multiplication table: ")
    )                                                           # get input from the user

for i in range(sideLength):
    row = ""                                                    # Initialize the variable that
                                                                # stores the values being printed
    
    for j in range(sideLength):       
        result = str((i+1)*(j+1))                               # Calculate the sum that to go in 
                                                                # each 'cell' of the table.
        
        padding = len(str(sideLength**2))*" "                   # Find the amount of padding 
                                                                # needed for the greatest value

        row += padding[len(str(value))-1:] + value + padding    # Insert the padding into the row
                                                                # currently being printed

    print(row)                                                  # Output the result