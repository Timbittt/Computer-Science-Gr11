#NAME:  Timofiy Kharchuk
#
#STUDENT NUMBER:  1008424
#
#ICS3U0 SECTION:  E
#
#OVERVIEW:  summary of function

print("Welcome to the IMS.")

def quitProgram():
    print("Quiting... ")
    return False

def help():
    print("This program is still currently in development.")

loop = True

while loop:
    command = input("Enter a command: ")

    if command == 'Q' or command == 'q':
        loop = quitProgram()
    
    elif command == 'H' or command == 'h':
        help()