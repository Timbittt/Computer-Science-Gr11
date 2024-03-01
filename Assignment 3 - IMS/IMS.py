#NAME:  Timofiy Kharchuk
#
#STUDENT NUMBER:  1008424
#
#ICS3U0 SECTION:  E
#
#OVERVIEW:  summary of function

print("Welcome to the IMS.")

loop = True

itemIds = []
itemPrices = []
itemDescriptions = []
itemStocks = []

def getItemIndex():
    itemId = input("Enter item id: ")

    if itemId in itemIds:
        itemIndex = itemIds.index(itemId)
        return itemIndex
    else:
        print("Item id not found")
        return "ERRORERRORERROR"

def help():
    print("This program is still currently in development.")

def quitProgram():
    print("Saving... ")
    saveFile()
    print("Quiting... ")
    return False

def listIds():
    print(*itemIds)

def printItemInfo():
    itemIndex = getItemIndex()

    if itemIndex == "ERRORERRORERROR":
        return

    print('\n', "----- Item info -----", '\n',
          " ID: ", itemIds[itemIndex], '\n',
          " Cost: ",itemPrices[itemIndex], '\n',
          " Desc: ", itemDescriptions[itemIndex], '\n',
          " Stock: ", itemDescriptions[itemIndex], '\n')
    
def removeItem():
    itemIndex = getItemIndex()

    if itemIndex == "ERRORERRORERROR":
        return
    
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
    newPrice = input("Enter new price: ")
    itemPrices[itemIndex] = newPrice
    print("Done.")

def changeItemDesc():
    itemIndex = getItemIndex()
    newDesc = input("Enter new description: ")
    itemDescriptions[itemIndex] = newDesc
    print("Done.")

def changeItemStock():
    itemIndex = getItemIndex()
    newStock = input("Enter new stock amount: ")
    itemStocks[itemIndex] = newStock
    print("Done.")

def changeItemId():
    itemIndex = getItemIndex()
    newID = input("Enter new item id: ")
    itemIds[itemIndex] = newID
    print("Done.")
   
def loadFile():
    global itemIds
    global itemPrices
    global itemDescriptions
    global itemStocks
    
    itemIds = []
    itemPrices = []
    itemDescriptions = []
    itemStocks = []
    
    inputFile = input("Enter name of input file or d for default: ")
    
    if(inputFile.lower() == 'd'): 
        inputFile = "data.txt"

    dataFile = open(inputFile)

    i = 0

    while True:
        line = dataFile.readline().rstrip('\n')

        if line == "ENDENDEND":
            break;
        
        match i % 4:
            case 0:
                itemIds.append(line)
            case 1:
                itemPrices.append(line)
            case 2:
                itemDescriptions.append(line)
            case 3:
                itemStocks.append(line)
        i += 1

    dataFile.close()

def saveFile():
    global itemIds
    global itemPrices
    global itemDescriptions
    global itemStocks

    outputFile = input("Enter name of file to save to or d for default: ")
    
    if(outputFile == 'd'): 
        outputFile = "data.txt"

    dataFile = open(outputFile, 'w')

    for i in range(len(itemIds)):
        dataFile.write(itemIds[i] + '\n' + 
                        itemPrices[i] + '\n' + 
                        itemDescriptions[i] + '\n' + 
                        itemStocks[i] + '\n')
    
    dataFile.write("ENDENDEND")

    dataFile.close()

def commandNotFound():
    print("The command entered does not exist, try again or enter h for a list of commands")

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

loadFile()
            
while loop:
    loop = checkInput()