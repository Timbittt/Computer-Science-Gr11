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
itemStock = []

def changePrice():
    return 0

def changeDesc():
    return 0

def changeStock():
    return 0

def loadFile():
    global itemIds
    global itemPrices
    global itemDescriptions
    global itemStock
    
    itemIds = []
    itemPrices = []
    itemDescriptions = []
    itemStock = []

    dataFile = open("data.txt")

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
                itemStock.append(line)

        print(i)
        i += 1

def saveFile():
    return 0

def quitProgram():
    print("Quiting... ")
    return False

def help():
    print("This program is still currently in development.")

def commandNotFound():
    print("The command entered does not exist, try again or enter h for a list of commands")

def checkInput(command):
    match command.lower():
        case 'p':
            changePrice()
        case 'd':
            changeDesc()
        case 'st':
            changeStock()
        case 'q':
            return quitProgram()
        case 'h':
            help()
        case 'save':
            saveFile()
        case 'load':
            loadFile()
        case _:
            commandNotFound()
    return loop

loadFile()
print(*itemIds)
print(*itemPrices)
print(*itemDescriptions)
print(*itemStock)


while loop:
    loop = checkInput(input("Enter a command: "))