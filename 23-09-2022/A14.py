# 14. Write a program to check the no is palindrome or not using function 

a = int(input("Enter the number "))

def palindrome(a):
    r = 0
    x = a

    while a > 0:
        r = r * 10 + a % 10
        a//=10

    return x == r

b = palindrome(a)

if b:
    print("palindrome")
else:
    print("not palindrome")

