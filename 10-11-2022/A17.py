# 2. WAP to take list of number and find which one is maximum.
l = [1,2,3,4,5,6,7,8,9,0]
m = l[0]
for i in l:
    if i > m:
        m = i
print(m)