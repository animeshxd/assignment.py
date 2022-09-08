# 10.wap to take a list of 10 number and store positive number in one list and negetive number in one list and display the list.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, -10]
p, n = [], []

for i in a:
    if i > 0:
        p.append(i)
    else:
        n.append(i)
print(a)
print('positive:', p)
print('negetive:', n)