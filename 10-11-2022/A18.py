# 3.WAP to take a list of number to print the duplicate number exists in the list or not .

l = [1,2, 2, 3,4,5,6,7,8,9,0]
s = set()
for i in l:
    if i in s:
        print(i)
    s.add(i)

