#NAME:  Timofiy Kharchuk
#
#STUDENT NUMBER:  1008424
#
#ICS3U0 SECTION:  E
#
#OVERVIEW:  summary of function

print("Welcome to the IMS.")

loop = True

ids = []
price = []
desc = []
stock = []

def changePrice(id, newPrice):
    price[id] = newPrice

def changeDesc(id, newDesc):
    desc[id] = newDesc

def changeStock(id, stockAmount):
    return 0

def changeId(oldId, newId):
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
        case 'id':
            changeId()
        case 'q':
            return quitProgram()
        case 'h':
            help()
        case _:
            commandNotFound()

    
    return loop

while loop:
    loop = checkInput(input("Enter a command: "))
