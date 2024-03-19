def solveQuadratic(a, b, c):
    if (not a) and (not b) and (not c):
        return -1, 0.0, 0.0
    if (not a) and (not b):
        return -2, 0.0, 0.0
    if not a:
        return 3, 2.0, 2.0

    root = b**2 - 4*a*c

    if root:
        return ( 2, ( -b + root**0.5 ) / ( 2*a ), ( -b - root**0.5 ) / ( 2*a ))
    else:
        return ( 1, (-b / (2 * a)), (-b / (2 * a)))
    

while True:
    print(solveQuadratic(int(input("Enter a: ")), int(input("Enter b: ")), int(input("Enter c: "))))