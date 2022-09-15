# 12. Write a program to calculate gcd of two numbers 

def gcd(a, b):
    if a == 0:
        return b
 
    return gcd(b % a, a)

a, b = map(int, input("Enter two number ").split())

x = gcd(a, b)
print(x, " is gcd of ", a,b)
