def drawSquare(length, char, style):
    if length < 1:
        print("Invalid Input: Side length must be a positive integer")
        return    
    
    if style.lower() == "solid" or length == 1:
        for i in range(length):
            print(char*length)

    elif style.lower() == "hollow":
        print(char+" "*(length-2)+char)

        for i in range(length):
            print(char*length)
        print(char+" "*(length-2)+char)

drawSquare(int(input("Enter side length: ")), input("Enter char: "), input("Enter style: "))