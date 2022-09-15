# 11. Write a program to display nth term of fibonacci series where n is given by user

n = int(input("Enter the number: "))
a = 0
b = 1
print(a,b)

for i in range(1, n-1):
    c = a + b;
    print(c);
    a = b;
    b = c;
    
