# 14. Write a program to check the no is palindrome or not using function 

a = int(input("Enter the number "))

r = 0
x = a

while a > 0:
    r = r * 10 + a % 10
    a//=10

if x == r:
    print("palindrome")
else:
    print("not palindrome")

