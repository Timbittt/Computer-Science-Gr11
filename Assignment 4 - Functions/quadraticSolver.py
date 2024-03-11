import math

def solveQuadratic(a, b, c):
    if not(a and b and c):
        return -1, 0.0, 0.0
    if not(a and b):
        return -2, 0.0, 0.0
    if not a:
        return 3, 0.0, 0.0

    root = b**2 - 4*a*c

    if root > 0:
        return ( 2, ( -b + math.sqrt(root) ) / ( 2*a ), ( -b - math.sqrt(root) ) / ( 2*a ) )
    elif root == 0:
        return ( 1, (-b / (2 * a)), (-b / (2 * a)))
    else:
        return (0, 0.0, 0.0)