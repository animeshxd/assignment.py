# 5.WAP to take list of 10 number and store even position number in saparate list and odd position number in saparate list and display the two list.
l = [1,2,3,4,5,6,7,8,9, 10]
e, o = [],[]

for i, j in enumerate(l):
    if j % 2 == 0:
        e.append(i)
    else:
        o.append(i)

print('even: ', e)
print('odd: ', o)
