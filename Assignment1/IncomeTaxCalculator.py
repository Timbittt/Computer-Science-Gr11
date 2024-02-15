while True:
    income = float(input("Enter your income (enter any negative value to quit): "))
    incomeTax = 0
    temp = income

    if income <= 0:
        break
    
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

    netIncome = income - incomeTax

    print("Your income is:    ", income)
    print("Your income tax is:", incomeTax)
    print("Your net income is:", netIncome)