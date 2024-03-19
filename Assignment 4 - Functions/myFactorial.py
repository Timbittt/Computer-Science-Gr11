def myFactorial(a):
    a = int(a)

    if a > 1:
        return a * myFactorial(a-1)
    else:
        return 1

print(myFactorial(input("Enter factorial to be calculated: ")))