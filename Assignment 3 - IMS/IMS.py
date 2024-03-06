#NAME:  Timofiy Kharchuk
#
#STUDENT NUMBER:  1008424
#
#ICS3U0 SECTION:  E
#
#OVERVIEW:  Allows the user to access and edit a database of different items

print("Welcome to the IMS.")

loop = True

# Initializing the arrays to store the info 
# that will be taken from the provided data file
itemIds = []
itemPrices = []
itemDescriptions = []
itemStocks = []

# Get the index of an item in order to make 
# changes to its id, price, description or id
def getItemIndex():
    itemId = input("Enter item id: ")

    # Make sure that the item id given exists
    if itemId in itemIds:
        itemIndex = itemIds.index(itemId)
        return itemIndex
    else:
        print("Item id not found")
        return "ERRORERRORERROR"

def help():
    print("+-----List of commands-----+",
          "\n   H - Help",
          "\n   Q - Quit",
          "\n   L - List all ids",
          "\n   I - Provide info for a given id",
          "\n   R - Remove an item",
          "\n   A - Add new item",
          "\n   P - Change the price of an item",
          "\n   D - Change item description",
          "\n   ST - Change item stock amount",
          "\n   ID - Change item id"
        )

def quitProgram():
    # Autosave when the program is exited to prevent lost data
    saveFile()

    print("Quiting... ")
    
    # Tell the main loop to stop running
    return False

def listIds():
    print(*itemIds)

def printItemInfo():
    itemIndex = getItemIndex()

    # Checking to see if getItemIndex()
    # failed to find the given id in
    # order to give the user an error message
    if itemIndex == "ERRORERRORERROR":
        return

    print('\n', "----- Item info -----", '\n',
          " ID: ", itemIds[itemIndex], '\n',
          " Cost: ",itemDescriptions[itemIndex], '\n',
          " Desc: ", itemPrices[itemIndex], '\n',
          " Stock: ", itemStocks[itemIndex], '\n')
    
def removeItem():
    itemIndex = getItemIndex()

    # Checking to see if getItemIndex()
    # failed to find the given id in
    # order to give the user an error message
    if itemIndex == "ERRORERRORERROR":
        return
    
    # Deleting the item info and then telling the user 
    # the info of the item they deleted so they 
    # know which item they successfuly deleted
    print("Deleted item with id:", itemIds.pop(itemIndex))
    del itemPrices[itemIndex]
    del itemDescriptions[itemIndex]
    del itemStocks[itemIndex]

def addNewItem():
    newId = input("Enter new item's id: ")
    newPrice = input("Enter new item's cost: ")
    newDesc = input("Enter new item's description: ")
    newStock = input("Enter the new item's stock: ")

    itemIds.append(newId)
    itemPrices.append(newPrice)
    itemDescriptions.append(newDesc)
    itemStocks.append(newStock)

    print("Item", newId, "added")

def changeItemPrice():
    itemIndex = getItemIndex()

    # Checking to see if getItemIndex()
    # failed to find the given id in
    # order to give the user an error message
    if itemIndex == "ERRORERRORERROR":
        return
    
    newPrice = input("Enter new price: ")
    
    itemPrices[itemIndex] = newPrice

    print("Done.")

def changeItemDesc():
    itemIndex = getItemIndex()

    # Checking to see if getItemIndex()
    # failed to find the given id in
    # order to give the user an error message
    if itemIndex == "ERRORERRORERROR":
        return
    
    newDesc = input("Enter new description: ")
    itemDescriptions[itemIndex] = newDesc
    print("Done.")

def changeItemStock():
    itemIndex = getItemIndex()

    # Checking to see if getItemIndex()
    # failed to find the given id in
    # order to give the user an error message
    if itemIndex == "ERRORERRORERROR":
        return
    
    newStock = input("Enter new stock amount: ")
    itemStocks[itemIndex] = newStock
    print("Done.")

def changeItemId():
    itemIndex = getItemIndex()

    # Checking to see if getItemIndex()
    # failed to find the given id in
    # order to give the user an error message
    if itemIndex == "ERRORERRORERROR":
        return
    
    newID = input("Enter new item id: ")
    itemIds[itemIndex] = newID
    print("Done.")
   
def loadFile():
    global itemIds
    global itemPrices
    global itemDescriptions
    global itemStocks
    
    # Clear item data in order to get rid of previous items
    itemIds = []
    itemPrices = []
    itemDescriptions = []
    itemStocks = []
    
    inputFile = input("Enter name of input file or d for default: ")
    
    # Let the user simply input a 'd' for a default file
    # instead of having to type out the whole file name
    if(inputFile.lower() == 'd'): 
        inputFile = "data.txt"

    dataFile = open(inputFile)

    # Groups every four lines in the input file to read the 
    # id; price; description; stock; format
    while True:
        line = dataFile.readline().rstrip('\n')

        # Checks if program reached the end of the file
        # to tell it to stop trying to read the file
        #
        # Also ends the program if it reads an empty string
        # for the item's id since it cannot be empty
        # in case there is no end file marker at the end
        # to keep the program from looping indefinitely
        if line == "ENDENDEND" or line == "":
            break

        itemIds.append(line)

        line = dataFile.readline().rstrip('\n')
        itemDescriptions.append(line)

        line = dataFile.readline().rstrip('\n')
        itemPrices.append(line)
                                
        line = dataFile.readline().rstrip('\n')
        itemStocks.append(line)

    dataFile.close()

def saveFile():
    global itemIds
    global itemPrices
    global itemDescriptions
    global itemStocks

    outputFile = input("Enter name of file to save to or d for default: ")

    print("Saving... ")
    
    # Let the user simply input a 'd' for a default file
    # instead of having to type out the whole file name
    if(outputFile == 'd'): 
        outputFile = "data.txt"

    dataFile = open(outputFile, 'w')

    for i in range(len(itemIds)):
        dataFile.write(itemIds[i] + '\n' + 
                        itemDescriptions[i] + '\n' + 
                        itemPrices[i] + '\n' + 
                        itemStocks[i] + '\n')
    
    dataFile.write("ENDENDEND")

    dataFile.close()

def commandNotFound():
    print("The command entered does not exist, try again or enter h for a list of commands")

# Runs the appropriate command based of the users input
def checkInput():
    command = input("Enter a command: ")

    match command.lower():
        case 'h':
            help()
        case 'q':
            return quitProgram()
        case 'l':
            listIds()
        case 'i':
            printItemInfo()
        case 'r':
            removeItem()
        case 'a':
            addNewItem()
        case 'p':
            changeItemPrice()
        case 'd':
            changeItemDesc()
        case 'st':
            changeItemStock()
        case 'id':
            changeItemId()
        case 'save':
            saveFile()
        case 'load':
            loadFile()
        case _:
            commandNotFound()
    return loop

# Get the initial data file from the user
loadFile()

# Code runs till the user quits so that the user can 
# do as many operations to the database 
# in a single sessions as necessary            
while loop:
    loop = checkInput()