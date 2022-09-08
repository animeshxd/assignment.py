# 3.wap to calculate area of triangle.  
import math

print("Enter three side of Triangle ")
A = int(input("1st side: "))
B = int(input("2nd side: "))
C = int(input("3rd side: "))

S = (A + B + C) / 2

AR = math.sqrt(S * (S - A) * (S - B) * (S - C))

print("Area:", AR)