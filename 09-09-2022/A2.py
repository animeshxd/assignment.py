# 2.wap to take 2 no and swap them without 3rd variable.

A = int(input("1st number: "))
B = int(input("2nd number: "))

print("numbers are:",A, B)
A, B = B, A
print("numbers are:", A, B)