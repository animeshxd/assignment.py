# 13. Write a program  to take a list of string and store all vowel in one list and other is another list and display them separately 

v = ['a','e','i','o','u']

l = input("Enter the list: ").split()

V, C = [], []


for i in l:
    if i.lower() in v:
        V.append(i)
    else:
        C.append(i)


print("Vowel", V)
print("Consonant", C)