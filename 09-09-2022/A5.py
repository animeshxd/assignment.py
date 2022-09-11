# 5.wap to find the roots of a quadratic equation.
import math

a, b, c = map(int, input('Enter the value of a, b, c : ').split())

d = b * b - 4 * a * c
if d == 0:
    x1 = -b / 2 * a
    print(x1,x1)
    
elif d > 0:

    x1 = (-b + math.sqrt(d))/2 * a
    x2 = (-b - math.sqrt(d))/2 * a
    print(x1,x2)
else:
    print("Imaginary Roots")
