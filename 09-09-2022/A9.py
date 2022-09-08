# 9.wap to take a list of 10 number and calculate even or odd.After calculate all even no stored in 1 list and stored odd numbers in another list and display them.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
e, o = [], []

for i in a:
    if i % 2 == 0:
        e.append(i)
    else:
        o.append(i)
        
print(a)
print('Even:', e)
print('Odd:', o)