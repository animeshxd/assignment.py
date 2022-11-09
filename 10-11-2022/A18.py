# 3.WAP to take a list of number to print the duplicate number exists in the list or not .

l = [1,2, 2, 3,4,5,6,7,8,9,0]
s = set()
f = True
for i in l:
    if i in s:
        print(i)
        f = False
    s.add(i)
if f:
    print("Dublicate number doesn't exists")

