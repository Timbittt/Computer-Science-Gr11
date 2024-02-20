#NAME:  Timofiy Kharchuk
#
#STUDENT NUMBER:  1008424
#
#ICS3U0 SECTION:  E
#
#OVERVIEW:  Calculates Income Tax and Net Income based off of an input of the user's income.

# Loops program forever till user quits
while True:
    # Gets input from user
    income = float(input("Enter your income (enter any negative value to quit): "))

    # Initializes variable to hold the amount of income tax the user has to pay
    incomeTax = 0
    
    # Used instead of income to find the amount of money in each bracket without mutating original income variable
    temp = income

    # Allows the user to quit the application by entering a negative number or 0
    if income <= 0:
        break
    
    # Finds the amount of the income that fits into each bracket and calculates the amount of tax
    if temp > 200000:
        amountOver = temp - 200000
        temp -= amountOver
        incomeTax += amountOver*0.40

    if temp > 120000:
        amountOver = temp - 120000
        temp -= amountOver
        incomeTax += amountOver*0.25

    if temp > 50000:
        amountOver = temp - 50000
        temp -= amountOver
        incomeTax += amountOver*0.20

    if temp > 10000:
        amountOver = temp - 10000
        temp -= amountOver
        incomeTax += amountOver*0.15

    # NOTE: Any income under $10,000 is not taxed, thus we don't need to deduct it

    # Finds the income after deducting tax
    netIncome = income - incomeTax

    # Outputs the users income, the amount of tax they need to pay, and their net income
    print("Your income is:    ", income)
    print("Your income tax is:", incomeTax)
    print("Your net income is:", netIncome)