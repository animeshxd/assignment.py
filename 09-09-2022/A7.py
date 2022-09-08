# 7.wap to take basic salary as input.
# DA is 15% of basic salary. HRA is 13% of BS.TA is 10% of basic salary. 
# If the gross salary is above 30000 then 10% tax will be deduct. What is the gross salary.

bs = int(input("Enter Basic Salary "))

da = bs * 0.15;
hra = bs * 0.13;
ta = bs * 0.10;
gs = bs + da + hra + ta;

if gs > 30000:
    gs -= gs * 0.10

print("gross salary:", gs)