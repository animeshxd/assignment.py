# 15. Write a program to take a number and check the number is armstrong or not using with parameters and return 

def armstrong(a):
    s = 0
    x = a
    while a > 0:
        s+= (a % 10) ** 3
        a//=10
    return x == s

x = int(input("Enter the number "))
a = armstrong(x)

if a:
    print(x, "is armstrong")
else:
    print(x, "is not armstrong")


    
